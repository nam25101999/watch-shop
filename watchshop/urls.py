# watchshop/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('products/', include('products.urls', namespace='products')),
    path('orders/', include('orders.urls')),
    path('cart/', include('cart.urls')),
    path('', include('users.urls')),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('messenger/', include('messenger.urls')),
    path('search/', include('search.urls', namespace='search')),


]

# Cấu hình hiển thị media (hình ảnh)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
