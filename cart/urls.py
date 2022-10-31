""" cart app urls file """
from django.urls import path
from . import views

urlpatterns = [
    path('view-cart/', views.view_cart, name='view_cart'),
    path('add/<event_id>', views.add_to_cart, name='add_to_cart'),
    path('amend-cart/<event_id>/', views.amend_cart, name='amend_cart'),
]
