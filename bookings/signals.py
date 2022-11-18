from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import BookingLineItem


@receiver(post_save, sender=BookingLineItem)
def update_post_save(sender, instance, created, **kwargs):
    """ Update booking total after item update/create and save """
    instance.booking.update_total()


@receiver(post_delete, sender=BookingLineItem)
def update_post_delete(sender, instance, **kwargs):
    """ update booking total after item deletion """
    instance.booking.update_total()
