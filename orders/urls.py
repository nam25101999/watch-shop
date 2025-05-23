# urls.py trong app orders
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('', views.order_list, name='order_list'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/<int:order_id>/edit-address/', views.edit_shipping_address, name='edit_shipping_address'),
    path('success/', views.order_success, name='order_success'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),

]
