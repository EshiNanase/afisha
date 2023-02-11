from django.contrib import admin
from places.models import Place, Image
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase


class ImageInLine(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview_image']
    list_display = ['get_preview_image', 'order']
    extra = 0

    def get_preview_image(self, obj):
        if not obj.image:
            return '-'
        return mark_safe(f'<img src="{obj.image.url}" height="{130}" />')

    get_preview_image.short_description = 'Image Preview'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInLine]
    fieldsets = (
        (None, {
            'fields': ('title', 'place_id', 'description_short', 'description_long', ('longitude', 'latitude'))
        }),
    )


admin.site.register(Image)
