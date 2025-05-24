from django.contrib import admin
from .models import (
    Brand, Category, Product, ProductImage,
)

# Đăng ký Brand, Category để dễ chọn trong Product
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'origin')
    search_fields = ('name', 'origin')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# Inline quản lý hình ảnh bổ sung cho sản phẩm
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Số form trống để thêm ảnh
    fields = ('image',)
    readonly_fields = ()

# Admin cho sản phẩm
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'brand', 'category', 'gender', 'price', 
        'stock', 'created_at'
    )
    list_filter = ('brand', 'category', 'gender')
    search_fields = ('name', 'description', 'specifications')
    ordering = ('-created_at',)

    # Các trường hiển thị trong form tạo/sửa sản phẩm
    fields = (
        'name', 'slug', 'brand', 'category', 'gender',
        'price', 'discount_price', 'stock',
        'description', 'specifications',
        'image',  # Ảnh chính
    )
    readonly_fields = ('slug',)  # Slug tự động tạo, không sửa thủ công

    inlines = [ProductImageInline]

    prepopulated_fields = {"slug": ("name",)}  # Tạo slug tự động

