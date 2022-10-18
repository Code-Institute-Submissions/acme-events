""" events app urls file """
from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventList.as_view(), name='event_list'),
    path("events/<slug:slug>/",
         views.EventDetailView.as_view(), name="event_detail"),
]
