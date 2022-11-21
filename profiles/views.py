from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from checkout.models import Booking
from .forms import UserProfileForm


def profile(request):
    """ Render user profile """

    template = 'profiles/profile.html'
    page_specific_title = 'Account'
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details updated successfully')

    form = UserProfileForm(instance=profile)
    bookings = profile.bookings.all()

    context = {
        'page_specific_title': page_specific_title,
        'profile': profile,
        'form': form,
        'bookings': bookings,
        'viewing_profile': True,
    }

    return render(request, template, context)


def booking_history(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)

    messages.info(request, (
        f'This is a past confirmation for booking id: {booking_id}. '
        'Confirmation was sent by email at the time of booking.'))

    template = 'checkout/checkout-success.html'
    context = {
        'booking': booking,
        'from_profile': True,
    }

    return render(request, template, context)
