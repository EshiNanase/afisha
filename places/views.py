from django.http import HttpResponse
from django.views.generic import TemplateView
from places.models import Place, Image
from django.templatetags.static import static
from django.conf import settings
import json


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

            details = {
                'title': place.title,
                'imgs': [image.image.url for image in Image.objects.filter(place=place)],
                'description_short': place.description_short,
                'description_long': place.description_long,
                'coordinates': {'lng': str(place.longitude), 'lat': str(place.latitude)}
            }

            self.data['features'].append(
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [place.longitude, place.latitude]
                    },
                    "properties": {
                        "title": place.title,
                        "placeId": place.place_id,
                        "detailsUrl": {}
                    }
                }
            )

        print(self.data)

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context['data'] = self.data

        return context
