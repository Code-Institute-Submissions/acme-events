from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User profile model for default checkout form
    values and booking history
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
        )
    default_street_address1 = models.CharField(
        max_length=150,
        null=True,
        blank=True
        )
    default_street_address2 = models.CharField(
        max_length=150,
        null=True,
        blank=True
        )
    default_city_or_town = models.CharField(
        max_length=150,
        null=True,
        blank=True
        )
    default_county = models.CharField(
        max_length=100,
        null=True,
        blank=True
        )
    default_postcode = models.CharField(
        max_length=15,
        null=True,
        blank=True
        )
    default_country = CountryField(
        blank_label='Country *',
        null=True,
        blank=True
        )
    default_telephone = models.CharField(
        max_length=25,
        null=True,
        blank=True
        )

    def __str__(self):
        return self.user.username
