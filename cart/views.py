from django.shortcuts import render
from django.contrib import messages


def cart(request):
    page_specific_title = 'Your Cart'
    context = {
        'page_specific_title': page_specific_title,
    }
    return render(request, 'cart/cart.html', context)