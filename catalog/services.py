from django.core.cache import cache
from django.db.models import QuerySet

from catalog.models import Category, Contact, Product
from config.settings import CACHE_ENABLED


def get_published_product_list() -> QuerySet:
    """
    load published products

    :return: QuerySet with all published products
    """
    queryset = Product.objects.filter(is_published=True)
    if CACHE_ENABLED:
        key = "published_products"
        products = cache.get(key)
        print(type(products))
        if products is None:
            products = queryset
            cache.set(key, products, 60 * 5)
        return products
    return queryset


def get_category_products(category_id: int) -> QuerySet:
    """
    load products from targeted category

    :param category_id: id of category
    :return: QuerySet with all published products in category
    """
    queryset = Product.objects.filter(is_published=True, product_category_id=category_id)
    if CACHE_ENABLED:
        key = f"category_{category_id}_products"
        products = cache.get(key)
        if products is None:
            products = queryset
            cache.set(key, products, 60 * 5)
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


def get_category_list() -> QuerySet:
    return Category.objects.all().order_by("category_name")
