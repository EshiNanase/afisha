from django.http import JsonResponse
from django.urls import reverse
from django.views.generic import DetailView, TemplateView

from places.models import Image, Place


class MapView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)

        data = {
            "type": "FeatureCollection",
            "features": []
        }

        places = Place.objects.all()
        for place in places:
            data['features'].append(
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [place.longitude, place.latitude]
                    },
                    "properties": {
                        "title": place.title,
                        "placeId": place.id,
                        "detailsUrl": reverse('place-detail', args=[place.id])
                    }
                }
            )
        context['data'] = data

        return context


class PlaceView(DetailView):

    def get(self, request, *args, **kwargs):
        place_id = self.kwargs['place_id']
        place = Place.objects.get(id=place_id)

        details = {
            'title': place.title,
            'imgs': [image.image.url for image in Image.objects.filter(place=place).order_by('order')],
            'description_short': place.description_short,
            'description_long': place.description_long,
            'coordinates': {'lng': str(place.longitude), 'lat': str(place.latitude)}
        }
        return JsonResponse(details)
