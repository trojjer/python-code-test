"""testsite URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

from shiptrader.views import StarshipViewSet, ListingViewSet


router = DefaultRouter()
router.register(r'starships', StarshipViewSet, basename='starship')
router.register(r'listings', ListingViewSet, basename='listing')

schema_view = get_swagger_view(title='Starship API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^swagger-docs/', schema_view),
    url(r'^api/v1/', include(router.urls))
]
