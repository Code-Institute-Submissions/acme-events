from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
# Above will make view require a POST request and reject GET requests
from django.views.decorators.csrf import csrf_exempt
# Stripe will not send CSRF token with webhook; must be exempt
from checkout.webhook_handler import StripeWH_Handler
# Custom class from file as named above

import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """
    This code comes from Stripe with some modifications from
    Boutique Ado. This function is returned by
    the 'wh/' path in checkout/urls.py Its purpose is to identify
    the type of event being sent by Stripe and then call the
    corresponding function from webhook_handler.py
    """

    # SetUp:
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature:
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        # Generic exception handler
        return HttpResponse(content=e, status=400)

    # Set up webhook handler by creating an instance
    # of it and passing in the request
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler
    event_map = {
        # Bug Notes (see README):
        # payment_intent.succeeded returns error500 in Stripe:
        # If replaced (e.g. with 'charge.succeeded': ...) will then be handled
        # by generic handler and the new event (e.g. charge.succeeded) will
        # return error 500 instead.
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }


    # Get the webhook type from Stripe
    event_type = event['type']

    # Assign this as the value of a variable called stripe_event_handler
    # stripe_event_handler is then an alias for whichever function you get
    # from the dictionary; give it the generic 'handle_stripe_event' by default
    stripe_event_handler = event_map.get(
        event_type, handler.handle_stripe_event)

    # Call the selected event handler function, passing it the event
    # received from Stripe:
    response = stripe_event_handler(event)
    return response
