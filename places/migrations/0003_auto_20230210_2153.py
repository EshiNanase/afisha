# Generated by Django 3.2.17 on 2023-02-10 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20230210_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
