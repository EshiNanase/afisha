import json

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('link', type=str)

    def handle(self, *args, **options):
        link = options['link']
        response = requests.get(link)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.find_all('td', class_='blob-code blob-code-inner js-file-line')
        data = ''
        for i in text:
            data += i.get_text()
        data = json.loads(data)

        place, created = Place.objects.get_or_create(
            title=data['title'],
            description_short=data['description_short'],
            description_long=data['description_long'],
            longitude=data['coordinates']['lng'],
            latitude=data['coordinates']['lat'],
        )

        for image in data['imgs']:
            obj, created = Image.objects.get_or_create(
                place=place,
                image_url=image
            )
            obj.get_image_from_url()
            obj.save()
