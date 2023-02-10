from django.db import models


class Place(models.Model):

    title = models.CharField(max_length=256)
    description_short = models.TextField()
    description_long = models.TextField()
    coordinates = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Image(models.Model):

    title = models.CharField(max_length=256)
    order = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return f'{self.order} {self.title}'
