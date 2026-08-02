from django.db.models import QuerySet
from django.core.cache import cache
from catalog.models import Contact, Product
from config.settings import CACHE_ENABLED


def get_published_product_list() -> QuerySet:
    queryset = Product.objects.filter(is_published=True)
    if CACHE_ENABLED:
        key = "products"
        products = cache.get('key')
        if products is None:
            products = queryset
            cache.set('key', products, 60 * 5)
        return products
    return queryset

def get_recent_products(number_of_products: int = 4) -> QuerySet:
    """
    Return last added products
    :param number_of_products: number of products to return, default: 4
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
