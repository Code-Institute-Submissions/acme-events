from django.contrib import admin
from .models import Event, Location


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'venue_name', 'street_address1', 'street_address2',
        'city_or_town', 'county', 'postcode', 'country',
        'telephone', 'website', 'map_link',
        )
    ordering = ('venue_name',)


class EventAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'location', 'start_date', 'start_time', 'published')

    ordering = ('start_date',)

    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Event, EventAdmin)
admin.site.register(Location)
