from django.db import models
from django.urls import reverse_lazy
from django.http import HttpRequest


class Place(models.Model):

    title = models.CharField(max_length=256)
    place_id = models.CharField(max_length=256)
    description_short = models.TextField()
    description_long = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):

    place = models.ForeignKey(to=Place, on_delete=models.CASCADE)
    order = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return f'{self.order} {self.place.title}'

    def get_absolute_url(self):
        return HttpRequest.build_absolute_uri(self.image.url)
