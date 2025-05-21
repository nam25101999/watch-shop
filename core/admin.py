from django.contrib import admin
from .models import Banner, StaticPage

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'link')
    list_filter = ('is_active',)
    search_fields = ('title',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="auto" />'
        return "(No image)"
    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'

@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('page',)
    search_fields = ('page',)
