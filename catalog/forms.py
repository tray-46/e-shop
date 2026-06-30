from django import forms
from catalog.models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ["product_name", "product_description", "image", "product_category", "price"]