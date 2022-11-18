""" checkout app urls file """
from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout-success/<booking_id>', views.checkout_success, name='checkout-success'),
]
