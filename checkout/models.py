import uuid
from django.db.models import Sum
from django.db import models

from events.models import Event


class Booking(models.Model):
    """
    Contain relevant info for bookings;
    Event specific details and quantity stored in BookingLineItem
    """

    first_name = models.CharField(
        verbose_name=('First Name'),
        max_length=60
        )
    last_name = models.CharField(
        verbose_name=('Last Name'),
        max_length=60
        )
    street_address1 = models.CharField(
        verbose_name=('StreetAddress1'),
        max_length=150
        )
    street_address2 = models.CharField(
        verbose_name=('StreetAddress2'),
        max_length=150,
        blank=True,
        null=True
        )
    city_or_town = models.CharField(
        verbose_name=('City/Town'),
        max_length=150
        )
    county = models.CharField(
        verbose_name=('County'),
        max_length=100
        )
    postcode = models.CharField(
        verbose_name=('Postcode'),
        max_length=15
        )
    country = models.CharField(
        verbose_name=('Country'),
        max_length=100,
        default="Ireland"
        )
    telephone = models.CharField(
        verbose_name=('Telephone'),
        max_length=25,
        null=False,
        blank=False
        )
    email = models.EmailField(
        verbose_name=('Email')
        )
    created_at = models.DateTimeField(
        verbose_name=('Booking Date'),
        auto_now_add=True
        )
    booking_id = models.UUIDField(
        verbose_name=('Booking ID'),
        primary_key=True,
        default=uuid.uuid4
        )
    booking_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
        )
    original_cart = models.TextField(
        null=False,
        blank=False,
        default=''
        )
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
        )

    def _create_booking_id(self):
        """
        Generate a random, unique booking id using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update total each time a booking line item is added
        """
        self.booking_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set booking number
        if it hasn't been set already.
        """
        if not self.booking_id:
            self.booking_id = self._create_booking_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.booking_id)


class BookingLineItem(models.Model):
    """
    LineItems represent individual events within a booking,
    although multiple instances of an identical event (ie. tickets) are
    regarded as one line item with a stated quantity,
    as in a standard invoice
    """
    booking = models.ForeignKey(
        Booking,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
        )
    event = models.ForeignKey(
        Event,
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0
        )
    lineitem_total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
        )

    def save(self, *args, **kwargs):
        """
        Override original save method to set the lineitem total
        and update booking_total
        """
        self.lineitem_total = self.event.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Event {self.event.name} on {self.event.start_date}'
