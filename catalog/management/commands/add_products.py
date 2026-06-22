"""
Command to populate catalog app database with example data.

Usage: python manage.py add_products
"""

from django.core.management import BaseCommand, call_command, CommandError
from catalog.models import Category, Product, Contact, Feedback


class Command(BaseCommand):

    help = "Add categories and products to catalog app database"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        Contact.objects.all().delete()
        Feedback.objects.all().delete()

        try:
            call_command("loaddata", "catalog_fixture.json", app="catalog", format="json", ignorenonexistent=True)
            self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
        except CommandError:
            self.stdout.write(self.style.ERROR("Failed to load data from fixture"))

        cat1, _ = Category.objects.get_or_create(category_name="Cat1", category_description="Cat1")

        products = [
            {"product_name": "Prod1", "product_description": "Prod 1", "product_category": cat1, "price": 1},
            {"product_name": "Prod2", "product_description": "Prod 2", "price": 1}
        ]

        for prod in products:
            _, created = Product.objects.get_or_create(**prod)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully created book: {prod["product_name"]}"))
            else:
                self.stdout.write(self.style.WARNING(f"Book already exists: {prod["product_name"]}."))
