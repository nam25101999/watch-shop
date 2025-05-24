from django.contrib import admin
from .models import Product, ProductImage, Brand

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'discount_price', 'stock', 'image_tag')
    readonly_fields = ('image_tag', 'created_at')
    search_fields = ('name', 'description', 'specifications')
    list_filter = ('brand',)

    fieldsets = (
        (None, {
            'fields': ('name', 'brand', 'price', 'discount_price', 'stock', 'image', 'image_tag', 'description', 'specifications')
        }),
    )

    def image_tag(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" />'
        return '(No Image)'
    image_tag.short_description = 'Hình ảnh'
    image_tag.allow_tags = True

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Brand)
