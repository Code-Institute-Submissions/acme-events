from django.http import HttpResponse

from .models import Booking, BookingLineItem
from events.models import Event as AcmeEvent
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        """ Assigns request as attribute of custom class """
        self.request = request
        print('wh_handler.py: __init__ method run')

    def handle_stripe_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event """
        print('wh_handler.py: Generic/Unknown webhook encountered')
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle payment intent succeeded webhooks from Stripe """
        print('running handle_payment_intent_succeeded')
        intent = event.data.object
        print('intent variable theoretically identified')
        print(intent)
        print('intent object should have been printed ABOVE THIS LINE')
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_detailss
        booking_total = round(intent.charges.data[0].amount / 100, 2)

        # Profile handling logic:
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            # Update profile information when save_info is checked
            # by extracting info from payment intent metadata 
            if save_info:
                profile.default_telehpone = billing_details.phone
                profile.default_street_address1 = billing_details.address.line1
                profile.default_street_address2 = billing_details.address.line2
                profile.default_city_or_town = billing_details.address.city
                profile.default_county = billing_details.address.state
                profile.default_postcode = billing_details.address.postal_code
                profile.default_country = billing_details.address.country
                profile.save()


        # Begin with booking_exists as False
        booking_exists = False
        
        # Set attempt counter to 1
        attempt = 1
        # While attempt is <= 5
        while attempt <= 5:
            # try to look-up a matching booking in the database
            try:
                # by matching the information in the Stripe intent
                booking = Booking.objects.get(
                    first_name__iexact=billing_details.name.split()[0],
                    email__iexact=billing_details.email,
                    telephone__iexact=billing_details.phone,
                    country__iexact=billing_details.address.country,
                    postcode__iexact=billing_details.address.postal_code,
                    city_or_town__iexact=billing_details.address.city,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    county__iexact=billing_details.address.state,
                    booking_total=total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                # Then set the booking_exists value to True
                booking_exists = True
                # and break out of the loop
                break
            except Booking.DoesNotExist:
                # if the booking does not exist on current attempt,
                attempt += 1
                # increment attempt counter by 1
                time.sleep(1)
                # sleep for 1 second
        # loop ends here; repeat or move on
        # if booking_exists is true by this time
        if booking_exists:
            # return 200 response to Stripe
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: \
                    Verified booking exists in database.',
                status=200)
        # if booking still doesn't exist, however,
        else:
            booking = None
            # set booking to None and then try to create the booking
            try:
                # using the data captured by Stripe
                booking = Booking.objects.create(
                    first_name=billing_details.name.split()[0],
                    last_name=billing_details.name.split(1)[1],
                    user_profile=profile,
                    email=billing_details.email,
                    telephone=billing_details.phone,
                    country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    city_or_town=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    county=billing_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                print(first_name)
                print(last_name)
                # being sure to use the json.dumps cart, not session cart
                # which may have expired due to browser closure
                for item_id, item_data in json.loads(cart).items():
                    event = AcmeEvent.objects.get(id=item_id)
                    booking_line_item = BookingLineItem(
                        booking=booking,
                        event=event,
                        quantity=item_data,
                        )
                    booking_line_item.save()
            # if booking cannot be reconstituted from Stripe data
            except Exception as e:
                # if booking has been partly created, delete it
                if booking:
                    booking.delete()
                # and return status 500 to Stripe
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR\
                        : {e}',
                    status=500)
        # if booking successfully created by webhook handler:
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: \
                Created booking in webhook', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle payment intent failed webhook from Stripe """
        print('wh_handler.py: Stage 4')
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
