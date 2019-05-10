import pytest

from rest_framework.test import APIClient


@pytest.fixture
def api_client(db):
    """
    API client fixture for testing endpoints.
    :param db: Fixture to enable DB access.
    :return: Instance of APIClient.
    """
    return APIClient()
