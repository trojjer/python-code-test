import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .tests.factories import StarshipFactory, ListingFactory


register(StarshipFactory)
register(ListingFactory)


@pytest.fixture
def api_client(db):
    """
    API client fixture for testing endpoints.
    :param db: Fixture to enable DB access.
    :return: Instance of APIClient.
    """
    return APIClient()
