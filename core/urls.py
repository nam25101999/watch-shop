from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('page/<str:page_slug>/', views.static_page_view, name='static_page'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),  # 👈 thêm trang liên hệ
]
