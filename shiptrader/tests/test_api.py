from django.urls import reverse
from rest_framework import status

from shiptrader.models import Starship, Listing


def test_get_starships(api_client, test_data):
    response = api_client.get(reverse('starship-list'))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 6


def test_get_listings(api_client, test_data):
    """All active Listings should be shown.
    """
    response = api_client.get(reverse('listing-list'))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5


def test_get_listing_detail(api_client, test_data):
    listing = Listing.objects.first()
    response = api_client.get(reverse('listing-detail', args=[listing.id]))

    assert response.status_code == status.HTTP_200_OK


def test_get_listings_by_starship_class(
        api_client, test_data, starship_factory, listing_factory):
    """Django-Filter backend should filter by related starship_class field.
    """
    new_ship = starship_factory(starship_class='Another Class')
    listing_factory(ship_type=new_ship)
    response = api_client.get(
        reverse('listing-list'), {'ship_type__starship_class': 'Another Class'})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


def test_get_listings_ordered_by_price(api_client, test_data, listing_factory):
    listing_factory(price=100)
    response = api_client.get(reverse('listing-list'), {'ordering': 'price'})

    assert response.status_code == status.HTTP_200_OK
    listings = response.data
    assert len(listings) == 6
    assert listings[0]['price'] == 100


def test_get_listings_ordered_by_price_descending(api_client, test_data, listing_factory):
    listing_factory(price=100)
    response = api_client.get(reverse('listing-list'), {'ordering': '-price'})

    assert response.status_code == status.HTTP_200_OK
    listings = response.data
    assert len(listings) == 6
    assert listings[5]['price'] == 100


def test_get_listings_ordered_by_modified(api_client, test_data, listing_factory):
    listing = listing_factory(name='New listing')
    response = api_client.get(reverse('listing-list'), {'ordering': 'modified'})

    assert response.status_code == status.HTTP_200_OK
    listings = response.data
    assert len(listings) == 6
    assert listings[5]['name'] == listing.name


def test_get_listings_ordered_by_modified_descending(api_client, test_data, listing_factory):
    listing = listing_factory(name='New listing')
    response = api_client.get(reverse('listing-list'), {'ordering': '-modified'})

    assert response.status_code == status.HTTP_200_OK
    listings = response.data
    assert len(listings) == 6
    assert listings[0]['name'] == listing.name


def test_create_listing(api_client, test_data):
    ship = Starship.objects.first()
    response = api_client.post(
        reverse('listing-list'),
        {
            'name': 'New listing',
            'ship_name': ship.name,
            'price': 666,
        },
        format='json'
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'New listing'
    assert response.data['ship_type'] == ship.id
    assert response.data['price'] == 666


def test_put_listing_deactivate(api_client, test_data):
    listing = Listing.objects.filter(is_active=True).first()
    response = api_client.patch(
        reverse('listing-detail', args=[listing.id]), {'is_active': False})

    assert response.status_code == status.HTTP_200_OK
    assert not response.data['is_active']
    listing = Listing.objects.get(id=listing.id)
    assert not listing.is_active


def test_put_listing_activate(api_client, test_data):
    listing = Listing.objects.filter(is_active=False).first()
    response = api_client.patch(
        reverse('listing-detail', args=[listing.id]), {'is_active': True})

    assert response.status_code == status.HTTP_200_OK
    assert response.data['is_active']
    listing = Listing.objects.get(id=listing.id)
    assert listing.is_active
