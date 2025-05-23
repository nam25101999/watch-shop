from django.db import models
from django.utils.translation import gettext_lazy as _

class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners/')
    link = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class StaticPage(models.Model):
    PAGE_CHOICES = [
        ('about', 'Giới thiệu'),
        ('contact', 'Liên hệ'),
        ('policy', 'Chính sách mua hàng'),
        ('return', 'Chính sách đổi trả'),
    ]
    page = models.CharField(max_length=20, choices=PAGE_CHOICES, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.get_page_display()
