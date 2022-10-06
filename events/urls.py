""" events app urls file """
from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventList.as_view(), name='event_list'),
]
