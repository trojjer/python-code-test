from django.urls import reverse


def test_get_starships(api_client, test_data):
    response = api_client.get(reverse('starship-list'))

    assert response.status_code == 200
    assert len(response.data) == 5


def test_get_listings(api_client, test_data):
    response = api_client.get(reverse('listing-list'))

    assert response.status_code == 200
    assert len(response.data) == 5


def test_get_listings_by_starship_class(
        api_client, test_data, starship_factory, listing_factory):
    """Django-Filter backend should filter by related starship_class field.
    """
    new_ship = starship_factory(starship_class='Another Class')
    listing_factory(ship_type=new_ship)
    response = api_client.get(
        reverse('listing-list'), {'ship_type__starship_class': 'Another Class'})

    assert response.status_code == 200
    assert len(response.data) == 1
