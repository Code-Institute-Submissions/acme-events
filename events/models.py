from django.db import models


class Location(models.Model):
    """ Locations for events """
    venue_name = models.CharField(max_length=250)
    street_address1 = models.CharField(max_length=150)
    street_address2 = models.CharField(max_length=150, blank=True, null=True)
    city_or_town = models.CharField(max_length=150)
    county = models.CharField(max_length=100)
    postcode = models.CharField(max_length=15)
    country = models.CharField(max_length=100, default="Ireland")
    telephone = models.CharField(max_length=25, null=False, blank=False)
    website = models.URLField(blank=True, null=True)
    map_link = models.URLField()

    def __str__(self):
        """ Standard string method returning venue_name field """
        return self.venue_name


class Event(models.Model):
    """
    Model for Event objects. Will later be connected to Booking objects
    """
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="events"
    )
    featured_image = models.ImageField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    published = models.BooleanField(default=False)

    def __str__(self):
        """ Standard string method returning name field """
        return self.name