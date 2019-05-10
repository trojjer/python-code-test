from django.urls import reverse


def test_get_starships(api_client, test_data):
    response = api_client.get(reverse('starship-list'))

    assert response.status_code == 200
    assert len(response.data) == 5
