# Generated by Django 3.2.12 on 2023-02-11 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_place_place_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='place_id',
        ),
    ]
