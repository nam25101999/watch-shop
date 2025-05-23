from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('send/', views.send_message, name='send_message'),
    path('admin/chat/', views.admin_chat_list, name='admin_chat_list'),
    path('admin/chat/<int:user_id>/', views.admin_chat, name='admin_chat'),
]
