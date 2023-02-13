# Generated by Django 3.2.12 on 2023-02-13 13:24

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_remove_place_place_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['order'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на изображение'),
        ),
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок изображений'),
        ),
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place', verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(null=True, verbose_name='Широота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(null=True, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
    ]
