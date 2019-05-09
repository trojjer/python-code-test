from django.db import models


class Starship(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    starship_class = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)

    length = models.FloatField()
    hyperdrive_rating = models.FloatField()
    cargo_capacity = models.BigIntegerField(default=0)

    crew = models.IntegerField()
    passengers = models.IntegerField()


class Listing(models.Model):
    name = models.CharField(max_length=255)
    ship_type = models.ForeignKey(Starship, related_name='listings')
    price = models.IntegerField()
