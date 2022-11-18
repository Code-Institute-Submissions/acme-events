from django.contrib import admin
from .models import Booking, BookingLineItem


class BookingLineItemAdminInline(admin.TabularInline):
    model = BookingLineItem
    readonly_fields = ('lineitem_total',)


class BookingAdmin(admin.ModelAdmin):
    inlines = (BookingLineItemAdminInline,)

    readonly_fields = ('booking_id', 'created_at', )

    fields = ('first_name', 'last_name', 'street_address1',
              'street_address2', 'city_or_town', 'county', 'postcode',
              'country', 'telephone', 'email', 'created_at',
              'booking_id', 'booking_total',)

    list_display = ('booking_id', 'created_at', 'first_name',
                    'last_name',)

    ordering = ('created_at',)


admin.site.register(Booking, BookingAdmin)
