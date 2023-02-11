from django.contrib import admin
from places.models import Place, Image


class ImageInLine(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInLine]


admin.site.register(Image)
