from rest_framework import viewsets, mixins
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from shiptrader.models import Starship, Listing
from shiptrader.serializers import StarshipSerializer, ListingSerializer


class StarshipViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset for browsing Starships.
    """
    serializer_class = StarshipSerializer
    queryset = Starship.objects.all()


class ListingViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    """
    Viewset for Listings.
    Allows the following:
       - Browse all Listings.
       - Retrieve a Listing by ID.
       - Creation of new Listing.
    TODO:
       - Filtering of Listings by starship_class param.
       - Activate/deactivate specific listing by ID.
    """
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, )
    filterset_fields = ('ship_type__starship_class', )
    ordering_fields = ('price', 'modified', )
