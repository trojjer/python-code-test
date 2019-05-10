import factory
from faker import Factory as FakerFactory


faker = FakerFactory.create()


class StarshipFactory(factory.django.DjangoModelFactory):
    """Model factory for Starships.
    """
    class Meta:
        model = 'shiptrader.Starship'

    name = factory.Sequence(lambda n: f'Ship {n}')
    model = factory.Sequence(lambda n: f'Model {n}')
    starship_class = 'Test Class'
    manufacturer = 'Acme Corp'
    length = 5000.0
    hyperdrive_rating = 1.5
    crew = 5
    passengers = 50


class ListingFactory(factory.django.DjangoModelFactory):
    """Model factory for Listings.
    """
    class Meta:
        model = 'shiptrader.Listing'

    name = factory.Sequence(lambda n: f'Listing {n}')
    price = 10000
