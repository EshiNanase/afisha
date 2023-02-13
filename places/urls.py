from django.urls import path

from places.views import MapView, PlaceView

app_name = 'places'

urlpatterns = [
    path('', MapView.as_view(), name='map-default'),
    path('places/<int:place_id>', PlaceView.as_view(), name='place-detail'),
]