from django.contrib import admin

from catalog.models import Category, Contact, Feedback, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin model"""

    list_display = (
        "id",
        "category_name",
    )
    search_fields = ("category_name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin model"""

    list_display = ("id", "product_name", "price", "product_category")
    search_fields = ("product_name", "product_description")
    list_filter = ("product_category",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Contact admin model"""

    list_display = ("id", "contact_country", "contact_name")
    search_fields = ("contact_name",)
    list_filter = ("contact_country",)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Contact admin model"""

    list_display = ("id", "feedback_username", "created_at", "processed")
    search_fields = ("feedback_username", "feedback_message")
    list_filter = (
        "processed",
        "feedback_username",
    )
    readonly_fields = (
        "id",
        "feedback_username",
        "feedback_phone",
        "feedback_message",
        "processed",
        "created_at",
    )
