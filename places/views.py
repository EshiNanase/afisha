from django.http import HttpResponse
from django.views.generic import TemplateView
from places.models import Place


class MapView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context['places'] = Place.objects.all()
        print(context['places'].first().coordinates)
        return context
