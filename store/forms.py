from django import forms
from .models import Product
from main.models import Category
class ProductForm(forms.ModelForm):
    class Meta:
        name = forms.CharField(widget=forms.TextInput({"class":"form-control", "placeholder":"Enter your product name"}), label="Product Name")

        model = Product
        fields = ['name', 'slug', 'description', 'price', 'image', 'stock', 'is_available', 'category']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'image']