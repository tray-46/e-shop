from django.contrib import admin
from catalog.models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin model"""
    list_display = ("id", "category_name",)
    search_fields = ("category_name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin model"""
    list_display = ("id", "product_name", "price", "product_category")
    search_fields = ("product_name", "product_description")
    list_filter = ("product_category",)
