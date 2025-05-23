from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Mỗi thuộc tính mở rộng sẽ là 1 model riêng để dùng làm ForeignKey
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

class WaterResistance(models.Model):  # Mức độ kháng nước
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    GENDER_CHOICES = [('male', 'Nam'), ('female', 'Nữ'), ('unisex', 'Unisex')]

    name = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    specifications = models.TextField()
    stock = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    watch_type = models.ForeignKey(WatchType, on_delete=models.SET_NULL, null=True, blank=True)
    style = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True, blank=True)
    dial = models.ForeignKey(Dial, on_delete=models.SET_NULL, null=True, blank=True)
    strap_material = models.ForeignKey(StrapMaterial, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    water_resistance = models.ForeignKey(WaterResistance, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/extra/')
