from django.http import HttpResponse
from django.views.generic import TemplateView


class MapView(TemplateView):
    template_name = 'index.html'