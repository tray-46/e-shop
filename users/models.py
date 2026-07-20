from typing import Optional

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """
    Represent site user

    Inherits from AbstractUser.
    Redefine username field to email.

    Attributes:
        first_name:
        last_name:
        email: (EmailField) Email address of user, required
        is_staff:
        is_active:
        date_joined:
        avatar: (ImageField) User's avatar, optional
        phone_number: (CharField) User phone number, optional
        country: (CharField) User country, optional
    """

    username: Optional[str] = None  # type: ignore[assignment]
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Введите Ваш email")
    avatar = models.ImageField(
        upload_to="users/avatars/", null=True, blank=True, verbose_name="Аватар", help_text="Загрузите аватар"
    )
    phone_number = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="Номер телефона", help_text="Введите номер телефона"
    )
    country = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Страна", help_text="Укажите вашу страну"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
