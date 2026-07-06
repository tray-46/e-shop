"""
Command to populate catalog app database with example data.

Usage: python manage.py add_products
"""

from typing import Any

from django.core.management import BaseCommand, CommandError, call_command

from catalog.models import Category, Contact, Feedback, Product
from blog.models import BlogPost


class Command(BaseCommand):

    help = "Add categories and products to catalog app database"

    def handle(self, *args: Any, **options: Any) -> None:
        Product.objects.all().delete()
        Category.objects.all().delete()
        Contact.objects.all().delete()
        Feedback.objects.all().delete()
        BlogPost.objects.all().delete()

        try:
            call_command("loaddata", "catalog_fixture.json", app="catalog", format="json", ignorenonexistent=True)
            self.stdout.write(self.style.SUCCESS("Successfully loaded catalog data from fixture"))
        except CommandError:
            self.stdout.write(self.style.ERROR("Failed to load catalog data from fixture"))

        try:
            call_command("loaddata", "blog_fixture.json", app="blog", format="json", ignorenonexistent=True)
            self.stdout.write(self.style.SUCCESS("Successfully loaded blog data from fixture"))
        except CommandError:
            self.stdout.write(self.style.ERROR("Failed to load blog data from fixture"))

        cat1, _ = Category.objects.get_or_create(category_name="Cat1", category_description="Cat1")

        products: list[dict[str, Any]] = [
            {"product_name": "Prod1", "product_description": "Prod 1", "product_category": cat1, "price": 1},
            {"product_name": "Prod2", "product_description": "Prod 2", "price": 1},
        ]

        for prod in products:
            _, created = Product.objects.get_or_create(**prod)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully created product: {prod["product_name"]}"))
            else:
                self.stdout.write(self.style.WARNING(f"Product already exists: {prod["product_name"]}."))
