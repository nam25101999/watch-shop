from django.shortcuts import render, get_object_or_404
from .models import Banner, StaticPage

# Hiển thị tất cả banner đang hoạt động (is_active=True)
def homepage_view(request):
    banners = Banner.objects.filter(is_active=True)
    return render(request, 'core/homepage.html', {'banners': banners})

# Hiển thị nội dung của một trang tĩnh (about, contact, policy, return)
def static_page_view(request, page_slug):
    page = get_object_or_404(StaticPage, page=page_slug)
    return render(request, 'core/static_page.html', {'page': page})

def about_view(request):
    return render(request, 'core/abouts.html')

def contact_view(request):
    return render(request, 'core/contact.html')