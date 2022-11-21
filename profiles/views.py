from django.shortcuts import render


def profile(request):
    """ Render user profile """

    template = 'profiles/profile.html'
    page_specific_title = 'Account'

    context = {
        'page_specific_title': page_specific_title,
    }

    return render(request, template, context)