# orders/forms.py
from django import forms
from .models import Order

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['recipient_name', 'phone_number', 'shipping_address', 'city', 'district', 'ward', 'postal_code']
        widgets = {
            'shipping_address': forms.Textarea(attrs={'rows': 2}),
        }
