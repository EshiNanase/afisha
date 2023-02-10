from django.db import models


class Place(models.Model):

    title = models.CharField(max_length=256)
    img_urls = models.TextField(null=True)
    description_short = models.TextField()
    description_long = models.TextField()
    coordinates = models.CharField(max_length=256)

    def __str__(self):
        return self.title
