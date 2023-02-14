from tempfile import NamedTemporaryFile
from urllib.request import urlopen

from django.core.files import File
from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):

    title = models.CharField(blank=False, max_length=256, verbose_name='Название')
    short_description = tinymce_models.HTMLField(blank=True, verbose_name='Короткое описание')
    long_description = tinymce_models.HTMLField(blank=True, verbose_name='Подробное описание')
    longitude = models.FloatField(null=False, verbose_name='Долгота')
    latitude = models.FloatField(null=False, verbose_name='Широта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):

    place = models.ForeignKey(null=False, to=Place, on_delete=models.CASCADE, verbose_name='Место')
    order = models.PositiveIntegerField(blank=True, default=0, verbose_name='Порядок изображений')
    image = models.ImageField(null=False, blank=False, verbose_name='Изображение')
    image_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на изображение')

    class Meta:
        ordering = ['order']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.order} {self.place.title}'

    def get_image_from_url(self):
        img_tmp = NamedTemporaryFile(delete=True)
        with urlopen(self.image_url) as uo:
            if uo.status == 200:
                img_tmp.write(uo.read())
                img_tmp.flush()
            else:
                raise ConnectionError
        img = File(img_tmp)
        self.image.save(f'{self.place.title}.jpg', img)
