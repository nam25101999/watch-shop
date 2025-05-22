# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
# forms.py
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'address', 'avatar', 'password1', 'password2')
