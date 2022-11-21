from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages


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