import uuid
from django.db import models


class Booking(models.Model):
    """
    Contain relevant info for bookings - still to add connection to event + quantity.
    Also to set up admin display fields.
    """

    first_name = models.CharField(verbose_name=('First Name'), max_length=60)
    last_name = models.CharField(verbose_name=('Last Name'), max_length=60)
    street_address1 = models.CharField(verbose_name=('StreetAddress1'), max_length=150)
    street_address2 = models.CharField(verbose_name=('StreetAddress2'), max_length=150, blank=True, null=True)
    city_or_town = models.CharField(verbose_name=('City/Town'), max_length=150)
    county = models.CharField(verbose_name=('County'), max_length=100)
    postcode = models.CharField(verbose_name=('Postcode'), max_length=15)
    country = models.CharField(verbose_name=('Country'), max_length=100, default="Ireland")
    telephone = models.CharField(verbose_name=('Telephone'), max_length=25, null=False, blank=False)
    email = models.EmailField(verbose_name=('Email'))
    created_at = models.DateTimeField(verbose_name=('Booking Date'), auto_now_add=True)
    booking_id = models.UUIDField(verbose_name=('Booking ID'), primary_key=True, default=uuid.uuid4)
    booking_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def __str__(self):
        return str(self.booking_id)
