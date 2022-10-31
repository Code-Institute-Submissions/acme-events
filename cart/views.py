from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib import messages

from events.models import Event


def view_cart(request):
    """ View shopping cart """
    page_specific_title = 'Your Cart'
    context = {
        'page_specific_title': page_specific_title,
    }
    return render(request, 'cart/cart.html', context)


def add_to_cart(request, event_id):
    """ Handles adding events to cart """
    redirect_url = request.POST.get('redirect_url')
    event = get_object_or_404(Event, pk=event_id)
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if event_id in list(cart.keys()):
        cart[event_id] += quantity
        messages.success(
            request, f'Updated ticket quantity to {cart[event_id]}')
    else:
        cart[event_id] = quantity
        messages.success(request, f'Added {event.name} to your cart')

    request.session['cart'] = cart

    return redirect(redirect_url)


def amend_cart(request, event_id):
    """Adjust the quantity of the specified item(s)"""

    event = get_object_or_404(Event, pk=event_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[event_id] = quantity
        messages.success(request, f'Quantity updated successfully.')
    else:
        cart.pop(event_id)
        messages.success(request, f'Removed {event.name} from your cart.')

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_from_cart(request, event_id):
    """Remove event entirely from cart"""
    try:
        event = get_object_or_404(Event, pk=event_id)
        cart = request.session.get('cart', {})
        cart.pop(event_id)
        messages.success(request, f'Removed {event.name} from your cart.')

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error: {e}')
        print(e)
        return HttpResponse(status=500)
