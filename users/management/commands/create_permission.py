from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        new_group, created = Group.objects.get_or_create(name='manager')
        ct_product = ContentType.objects.get_for_model(Product)

        change_product = Permission.objects.get(codename='change_product', name='Can change продукт', content_type=ct_product)

        new_group.permissions.add(change_product)