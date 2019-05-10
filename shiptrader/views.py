from rest_framework import viewsets

from shiptrader.models import Starship
from shiptrader.serializers import StarshipSerializer


class StarshipViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset for browsing Starships.
    """
    serializer_class = StarshipSerializer
    queryset = Starship.objects.all()
