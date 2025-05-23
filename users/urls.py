# urls.py
from django.urls import path
from .views import register_view, login_view, logout_view, account_view, update_account_view

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('account/', account_view, name='account'),
    path('account/update/', update_account_view, name='update_account'),
]
