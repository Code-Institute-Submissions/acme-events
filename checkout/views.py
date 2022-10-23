from django.shortcuts import render


def cart(request):
    return render(request, 'checkout/cart.html')
