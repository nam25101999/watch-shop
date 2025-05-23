from django.db import models
from django.utils.text import slugify

class Brand(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WatchType(models.Model):  # Loại đồng hồ
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Style(models.Model):  # Phong cách
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dial(models.Model):  # Mặt đồng hồ
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StrapMaterial(models.Model):  # Chất liệu dây
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Color(models.Model):  # Màu sắc
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WaterResistance(models.Model):  # Kháng nước
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Các model bổ sung theo yêu cầu
class Movement(models.Model):  # Bộ máy
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Glass(models.Model):  # Mặt kính
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CaseDiameter(models.Model):  # Đường kính mặt (vd: "40mm")
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.size

class SpecialEdition(models.Model):  # Phiên bản đặc biệt
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DialShape(models.Model):  # Hình dạng mặt số
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Feature(models.Model):  # Tính năng
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Origin(models.Model):  # Nguồn gốc
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country

class SortOrder(models.Model):  # Sắp xếp
    order = models.PositiveIntegerField()
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.order} - {self.description}"


class Product(models.Model):
    GENDER_CHOICES = [
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('unisex', 'Unisex'),
    ]

    name = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    discount_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    specifications = models.TextField()
    stock = models.PositiveIntegerField()
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    watch_type = models.ForeignKey(WatchType, on_delete=models.SET_NULL, null=True, blank=True)
    style = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True, blank=True)
    dial = models.ForeignKey(Dial, on_delete=models.SET_NULL, null=True, blank=True)
    strap_material = models.ForeignKey(StrapMaterial, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    water_resistance = models.ForeignKey(WaterResistance, on_delete=models.SET_NULL, null=True, blank=True)

    # Các thuộc tính bổ sung
    movement = models.ForeignKey(Movement, on_delete=models.SET_NULL, null=True, blank=True)
    glass = models.ForeignKey(Glass, on_delete=models.SET_NULL, null=True, blank=True)
    case_diameter = models.ForeignKey(CaseDiameter, on_delete=models.SET_NULL, null=True, blank=True)
    special_edition = models.ForeignKey(SpecialEdition, on_delete=models.SET_NULL, null=True, blank=True)
    dial_shape = models.ForeignKey(DialShape, on_delete=models.SET_NULL, null=True, blank=True)
    feature = models.ForeignKey(Feature, on_delete=models.SET_NULL, null=True, blank=True)
    origin = models.ForeignKey(Origin, on_delete=models.SET_NULL, null=True, blank=True)
    sort_order = models.ForeignKey(SortOrder, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/extra/')

    def __str__(self):
        return f"Ảnh cho {self.product.name}"
