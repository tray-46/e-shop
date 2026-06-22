from django.db import models


# Create your models here.
class Category(models.Model):
    """
    Store a single product category

    Attributes:
        category_name (CharField): Category name
        category_description (TextField): Category description
    """

    category_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории продуктов",
    )
    category_description = models.TextField(
        verbose_name="Описание категории", help_text="Введите описание категории продуктов"
    )

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

    product_name = models.CharField(
        max_length=250, verbose_name="Наименование продукта", help_text="Введите наименование продукта"
    )
    product_description = models.TextField(verbose_name="Описание продукта", help_text="Введите описание продукта")
    image = models.ImageField(
        upload_to="products/",
        null=True,
        blank=True,
        verbose_name="Изображение продукта",
        help_text="Загрузите изображение продукта",
    )
    product_category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Категория продукта",
        help_text="Выберите катагорию продуктов",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за покупку", help_text="Введите цену продукта")
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


class Contact(models.Model):
    """
    Store a single contact information

    Attributes:

    """
    contact_country = models.CharField(max_length=50, verbose_name="Страна", help_text="Введите название страны")
    contact_name = models.CharField(max_length=150, verbose_name="Наименование", help_text="Введите наименование контакта")
    contact_address = models.CharField(max_length=250, verbose_name="Адрес", help_text="Введите адрес")
    contact_email = models.EmailField(verbose_name="e-mail", help_text="Введите адрес электронной почты")
    contact_phone = models.CharField(max_length=15, verbose_name="Телефон", help_text="Введите номер телефона")

    class Meta:
        """Meta options for Contact model"""
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["contact_country"]

    def __str__(self) -> str:
        """Return string representation of Contact"""
        return f"{self.contact_name}, {self.contact_country}"


class Feedback(models.Model):
    """
    Store a single contact information

    Attributes:

    """
    feedback_username = models.CharField(max_length=150, verbose_name="Имя")
    feedback_phone = models.CharField(max_length=15, verbose_name="Телефон")
    feedback_message = models.TextField(verbose_name="Сообщение")
    processed = models.BooleanField(default=False, verbose_name="Обработан")  # имя так себе =(
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        """Meta options for Contact model"""
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["created_at"]

    def __str__(self) -> str:
        """Return string representation of Contact"""
        return f"{self.feedback_username} - {self.created_at}"

