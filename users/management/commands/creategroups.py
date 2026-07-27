from typing import Any

from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create groups"

    def handle(self, *args: Any, **options: Any) -> None:
        product_moderators, _ = Group.objects.get_or_create(name="Product_moderators")
        product_unpublish_permission = Permission.objects.get(codename="can_unpublish_product")
        product_delete_permission = Permission.objects.get(codename="delete_product")
        product_moderators.permissions.add(product_unpublish_permission, product_delete_permission)
        product_moderators.save()

        content_managers, _ = Group.objects.get_or_create(name="Content_managers")
        blogpost_add_permission = Permission.objects.get(codename="add_blogpost")
        blogpost_change_permission = Permission.objects.get(codename="change_blogpost")
        blogpost_delete_permission = Permission.objects.get(codename="delete_blogpost")
        content_managers.permissions.add(
            blogpost_add_permission, blogpost_change_permission, blogpost_delete_permission
        )
        content_managers.save()

        self.stdout.write(self.style.SUCCESS("Groups successfully added"))
