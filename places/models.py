from tempfile import NamedTemporaryFile
from urllib.request import urlopen

from django.core.files import File
from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    description_short = tinymce_models.HTMLField(verbose_name='Короткое описание')
    description_long = tinymce_models.HTMLField(verbose_name='Подробное описание')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):

    place = models.ForeignKey(to=Place, on_delete=models.CASCADE, verbose_name='Место')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок изображений')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
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
            assert uo.status == 200
            img_tmp.write(uo.read())
            img_tmp.flush()
        img = File(img_tmp)
        self.image.save(f'{self.place.title}.jpg', img)
