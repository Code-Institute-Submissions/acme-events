from django.shortcuts import get_object_or_404
from events.models import Event


def cart_contents(request):
    """
    Context Processor for handling user's session-specific cart.
    Made available via settings.py.
    """
    cart_items = []
    total = 0
    ticket_count = 0
    cart = request.session.get('cart', {})
    # identify or create 'cart' variable for session

    for event_id, quantity in cart.items():
        event = get_object_or_404(Event, pk=event_id)
        subtotal = quantity * event.price
        cart_items.append({
            'event_id': event_id,
            'quantity': quantity,
            'event': event,
            'subtotal': subtotal,
        })
        total += quantity * event.price
        ticket_count += quantity

    context = {
        'cart_items': cart_items,
        'total': total,
        'ticket_count': ticket_count,
    }

    return context
