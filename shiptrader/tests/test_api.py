from django.urls import reverse


def test_get_starships(api_client):
    response = api_client.get(reverse('starship-list'))

    assert response.status_code == 200
