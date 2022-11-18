from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from django.conf import settings

from events.models import Event
from .models import Booking, BookingLineItem
from .forms import CheckoutForm
from cart.contexts import cart_contents

import stripe
import json


def checkout(request):
    """ Render checkout page and/or handle checkout form """

    page_specific_title = 'Checkout'
    print('stage 1')

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        print('post method identified')
        # checkout form handling
        cart = request.session.get('cart', {})
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'telephone': request.POST['telephone'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'city_or_town': request.POST['city_or_town'],
            'postcode': request.POST['postcode'],
            'county': request.POST['county'],
            'country': request.POST['country'],
        }
        print('form data identified')
        checkout_form = CheckoutForm(form_data)
        if checkout_form.is_valid():
            print('form found valid')
            booking = checkout_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            booking.stripe_pid = pid
            print('string info identified')
            booking.save()
            for item_id, item_data in cart.items():
                try:
                    print('entered try block')
                    event = Event.objects.get(id=item_id)
                    booking_line_item = BookingLineItem(
                        booking=booking,
                        event=event,
                        quantity=item_data,
                    )
                    print('completed declaration portion of try block')
                    booking_line_item.save()
                    print('line item saved')
                except Event.DoesNotExist:
                    messages.error(request, (
                        "One of the events in your cart no longer exists \
                            within our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))
            print('form data saved')
            request.session['save_info'] = 'save-info' in request.POST
            print(5)
            return redirect(
                reverse('checkout-success', args=[booking.booking_id]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
            print(6)
    else:
        checkout_form = CheckoutForm()
        template = 'checkout/checkout.html'
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, 'You currently have no items in your cart')
            return redirect(reverse('event_list'))
        # Stripe payment variables
        current_cart = cart_contents(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )

    if not stripe_public_key:
        messages.warning(request, 'Error: Contact developer/site owner and \
            quote this error message: Stripe public key missing from \
            environment. ')

    context = {
            'page_specific_title': page_specific_title,
            'checkout_form': checkout_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
            'stripe_total': stripe_total,
        }

    return render(request, template, context)


def checkout_success(request, booking_id):
    """
    Handle successful checkouts
    """
    page_specific_title = 'Success'
    save_info = request.session.get('save_info')
    booking = get_object_or_404(Booking, booking_id=booking_id)
    messages.success(request, f'Booking successfully processed!')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout-success.html'
    context = {
        'page_specific_title': page_specific_title,
        'booking': booking,
    }

    return render(request, template, context)
