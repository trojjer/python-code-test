from django.urls import reverse


def test_get_starships(api_client, starship_factory):
    ships = [starship_factory() for s in range(5)]
    response = api_client.get(reverse('starship-list'))

    assert response.status_code == 200
    assert len(response.data) == 5
