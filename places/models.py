from django.db import models
from tinymce import models as tinymce_models
from django.core.files import File
from django.core.files.images import ImageFile
from urllib.request import urlopen
from tempfile import NamedTemporaryFile


class Place(models.Model):

    title = models.CharField(max_length=256)
    description_short = tinymce_models.HTMLField()
    description_long = tinymce_models.HTMLField()
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):

    place = models.ForeignKey(to=Place, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order} {self.place.title}'

    def get_image_from_url(self):
        img_tmp = NamedTemporaryFile(delete=True)
        with urlopen(self.image_url) as uo:
            assert uo.status == 200
            img_tmp.write(uo.read())
            img_tmp.flush()
        img = File(img_tmp)
        self.image.save(f'{self.place.title}', img)

