from django.db.models import QuerySet

from catalog.models import Contact, Product


def get_recent_products(number_of_products: int = 4) -> QuerySet:
    """
    Return last added products
    :param number_of_products (int0: number of products to return, default: 4
    :return (QuerySet): last added products
    """
    products = Product.objects.order_by("-created_at")[:number_of_products]
    return products


def get_contacts() -> QuerySet:
    """
    Return contacts
    :return (QuerySet): all contacts:
    """
    return Contact.objects.all().order_by("id")
