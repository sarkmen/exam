from django import forms
from .models import Category, Shop, Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', ]


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'phone', 'address', 'intro', 'image1', 'image2', 'image3',]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['message', 'image',]