import os

from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            DJANGO_SU_NAME = os.environ.get("DJANGO_SUPERUSER")
            DJANGO_SU_EMAIL = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
            DJANGO_SU_PASSWORD = os.environ.get("DJANGO_SUPERUSER_EMAIL")
            super_user = User.objects.create_superuser(
                username=DJANGO_SU_NAME,
                password=DJANGO_SU_PASSWORD,
                email=DJANGO_SU_EMAIL)
            super_user.is_superuser = True

            super_user.save()
