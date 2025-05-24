from django.urls import path
from .views import (
    create_order,
    order_list,
    edit_shipping_address,
    checkout,
    order_payment,
    order_success,
    order_detail,
    payment_view,
    payment_confirmation,
    payment_bank,
    payment_cod,
    payment_momo,
)

app_name = 'orders'

urlpatterns = [
    path('create/', create_order, name='create_order'),
    path('', order_list, name='order_list'),
    path('edit-shipping/<int:order_id>/', edit_shipping_address, name='edit_shipping_address'),
    path('checkout/', checkout, name='checkout'),
    path('payment/<int:order_id>/', order_payment, name='order_payment'),
    path('success/', order_success, name='order_success'),
    path('detail/<int:order_id>/', order_detail, name='order_detail'),
    path('payment/view/<int:order_id>/', payment_view, name='payment_view'),
    path('payment/confirmation/<int:order_id>/', payment_confirmation, name='payment_confirmation'),
    path('payment/bank/<int:order_id>/', payment_bank, name='payment_bank'),
    path('payment/cod/<int:order_id>/', payment_cod, name='payment_cod'),
    path('payment/momo/<int:order_id>/', payment_momo, name='payment_momo'),
]
