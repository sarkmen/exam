from django import forms
from .models import Category, Shop

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', ]


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'phone', 'address', 'intro', 'image1', 'image2', 'image3',]