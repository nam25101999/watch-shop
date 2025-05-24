from django.contrib import admin
from .models import (
    Brand, Category, Product, ProductImage,
    WatchType, Style, Dial, StrapMaterial, Color, WaterResistance,
    Movement, Glass, CaseDiameter, SpecialEdition, DialShape,
    Feature, Origin, SortOrder
)

# Đăng ký các model phụ để quản lý dễ dàng nếu muốn
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'origin')
    search_fields = ('name', 'origin')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(WatchType)
class WatchTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Dial)
class DialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(StrapMaterial)
class StrapMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(WaterResistance)
class WaterResistanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Glass)
class GlassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(CaseDiameter)
class CaseDiameterAdmin(admin.ModelAdmin):
    list_display = ('id', 'size')

@admin.register(SpecialEdition)
class SpecialEditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(DialShape)
class DialShapeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('id', 'country')

@admin.register(SortOrder)
class SortOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'description')
    ordering = ('order',)


# Inline để quản lý hình ảnh trong trang chỉnh sửa sản phẩm
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'brand', 'category', 'gender', 'price', 
        'discount_price', 'stock', 'is_featured', 'created_at'
    )
    list_filter = (
        'brand', 'category', 'gender', 'is_featured', 'watch_type',
        'style', 'dial', 'strap_material', 'color', 'water_resistance',
        'movement', 'glass', 'case_diameter', 'special_edition',
        'dial_shape', 'feature', 'origin',
    )
    search_fields = ('name', 'description', 'specifications')
    ordering = ('-created_at',)
    inlines = [ProductImageInline]
    prepopulated_fields = {"slug": ("name",)}  # Tự động tạo slug từ tên

