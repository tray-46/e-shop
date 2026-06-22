from django.db.models import QuerySet

from catalog.models import Product

def get_recent_products(number_of_products: int = 4) -> QuerySet:
    """
    Return last added products
    :param number_of_products (int0: number of products to return, default: 4
    :return (QuerySet): last added products
    """
    products = Product.objects.all()[:number_of_products]
    return products
