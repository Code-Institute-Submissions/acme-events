from django.shortcuts import render


def index(request):
    """ Returns index page """

    template_name = 'index'

    context = {
        'template_name': template_name,
    }

    return render(request, 'home/index.html', context)
