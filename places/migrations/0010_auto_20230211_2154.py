# Generated by Django 3.2.12 on 2023-02-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_image_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
