from django.db import models


# Create your models here.
class Category(models.Model):
    """
    Store a single product category

    Attributes:
        category_name (CharField): Category name
        category_description (TextField): Category description
    """
    category_name = models.CharField(max_length=100, unique=True, verbose_name="Наименование категории",
                                     help_text="Введите наименование категории продуктов")
    category_description = models.TextField(verbose_name="Описание категории",
                                            help_text="Введите описание категории продуктов")

    class Meta:
        """Meta options for Category model"""
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["category_name"]

    def __str__(self) -> str:
        """Return string representation of Category"""
        return self.category_name


class Product(models.Model):
    """
    Store a single product

    Attributes:
        product_name (CharField): Product name
        product_description (TextField): Product description
        image (ImageField): Product image
        product_category (ForeignKey): Product category
        price (DecimalField): Product price
        created_at (DateTimeField): Product creation date
        updated_at (DateTimeField): Product update date
    """
    product_name = models.CharField(max_length=250, verbose_name="Наименование продукта",
                                    help_text="Введите наименование продукта")
    product_description = models.TextField(verbose_name="Описание продукта", help_text="Введите описание продукта")
    image = models.ImageField(upload_to="products/", null=True, blank=True, verbose_name="Изображение продукта",
                              help_text="Загрузите изобрадение продукта")
    product_category = models.ForeignKey(Category, related_name="products", on_delete=models.SET_NULL, null=True,
                                         blank=True, verbose_name="Категория продукта",
                                         help_text="Выберите катагорию продуктов")
    price = models.DecimalField(decimal_places=2, verbose_name="Цена за покупку", help_text="Введите цену продукта")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    class Meta:
        """Meta options for Product model"""
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["product_name"]

    def __str__(self) -> str:
        """Return string representation of Product"""
        return self.product_name
