from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'content', 'created_at']
    list_filter = ['created_at']

admin.site.register(Review, ReviewAdmin)
