from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):

    readonly_fields = ('booking_id', 'created_at', )

    fields = ('first_name', 'last_name', 'email', 'created_at', 'booking_id')

    list_display = ('booking_id', 'created_at', 'first_name',
                    'last_name',)

    ordering = ('created_at',)


admin.site.register(Booking, BookingAdmin)
