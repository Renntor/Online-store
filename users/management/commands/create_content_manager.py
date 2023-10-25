from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import Blog


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        new_group, created = Group.objects.get_or_create(name='content_manager')
        ct_blog = ContentType.objects.get_for_model(Blog)

        change_product = Permission.objects.get(codename='change_blog', name='Can change блог',
                                                content_type=ct_blog)

        new_group.permissions.add(change_product)
