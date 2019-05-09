from itertools import chain

import requests
from requests.exceptions import HTTPError
from django.core.management.base import BaseCommand

from shiptrader.serializers import StarshipSerializer
from shiptrader.models import Starship
from testsite.settings import STARSHIP_URI


class Command(BaseCommand):
    help = 'Import data from the remote Starship API and creates models as needed.'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = requests.Session()

    def handle(self, *args, **options):
        self.stdout.write('Connecting to Starship API...')
        ship_data = list(chain.from_iterable(self.get_data()))
        self.stdout.write(f'Retrieved {len(ship_data)} ships.')

        self.stdout.write('Creating Starship instances')
        ships = StarshipSerializer(data=ship_data, many=True)
        if ships.is_valid():
            ships.save()
            self.stdout.write(f'DB record count: {Starship.objects.count()}')
        else:
            self.stderr.write(f'Problem validating ship data: {ships.errors}')

    def get_data(self):
        """
        Generator to retrieve all results from a paginated JSON source.
        :yield: List of results from current page.
        """
        try:
            this_page = self.session.get(STARSHIP_URI)
            this_page.raise_for_status()
        except HTTPError as http_error:
            self.stderr.write(f'Problem accessing ship data: {http_error}')
            raise
        else:
            this_page = this_page.json()
            yield this_page['results']

        while this_page['next']:
            next_page = this_page['next']
            self.stdout.write(next_page)
            this_page = self.session.get(next_page).json()
            yield this_page['results']
