from django.shortcuts import render
from .forms import BookingForm


def cart(request):
    page_specific_title = 'Your Cart'
    context = {
        'page_specific_title': page_specific_title,
    }
    return render(request, 'checkout/cart.html', context)


def checkout(request):
    """ Stripe keys to be added """

    template = 'checkout/checkout.html'
    page_specific_title = 'Checkout'

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
        booking_form = BookingForm(form_data)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
    else:
        booking_form = BookingForm()

    context = {
            'page_specific_title': page_specific_title,
            'booking_form': booking_form,
        }

    return render(request, template, context)
