from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from places.models import Image, Place


class ImageInLine(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview_image']
    list_display = ['get_preview_image', 'order']
    extra = 0

    def get_preview_image(self, obj):
        if not obj.image:
            return '-'
        return format_html('<img src="{}" height="{}" />',
                           obj.image.url, 130)

    get_preview_image.short_description = 'Image Preview'


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    model = Image


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInLine]
    fieldsets = (
        (None, {
            'fields': ('title', 'short_description', 'long_description', ('longitude', 'latitude'))
        }),
    )
