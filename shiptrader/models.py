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

    def __str__(self):
        return f'{self.name} made by {self.manufacturer}'


class Listing(models.Model):
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    ship_type = models.ForeignKey(Starship, related_name='listings')
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Listing for {self.ship_type} at price {self.price}'

