from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import CheckoutForm

import stripe
import json


def checkout(request):
    """ Stripe keys to be added """

    template = 'checkout/checkout.html'
    page_specific_title = 'Checkout'

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'county': request.POST['county'],
            'country': request.POST['country'],
        }
        checkout_form = CheckoutForm(form_data)
        if checkout_form.is_valid():
            booking = checkout_form.save(commit=False)
    else:
        checkout_form = CheckoutForm()

    context = {
            'page_specific_title': page_specific_title,
            'checkout_form': checkout_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': 'temporary',
        }

    return render(request, template, context)
