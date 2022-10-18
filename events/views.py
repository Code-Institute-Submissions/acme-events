from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from .models import Event


class EventList(ListView):
    model = Event
    template_name = "events/event-list.html"


class EventDetailView(DetailView):
    model = Event
    template_name = "events/event-detail.html"
