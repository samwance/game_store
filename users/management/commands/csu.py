from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            phone="12345678",
            is_superuser=True,
            is_staff=True,
            is_active=True,
            name="admin",
        )

        user.set_password("12345")
        user.save()
