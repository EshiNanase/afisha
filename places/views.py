from django.views.generic import TemplateView, DetailView
from places.models import Place, Image
from django.http import JsonResponse
from django.urls import reverse


class MapView(TemplateView):
    template_name = 'index.html'

    def __init__(self):
        super(MapView, self).__init__()

        self.data = {
              "type": "FeatureCollection",
              "features": []
            }

        places = Place.objects.all()
        for place in places:

            self.data['features'].append(
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

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context['data'] = self.data

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
