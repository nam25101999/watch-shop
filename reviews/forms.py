# reviews/forms.py
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label="Nội dung đánh giá")

    class Meta:
        model = Review
        fields = ['content']
