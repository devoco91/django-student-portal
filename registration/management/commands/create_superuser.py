from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError, ProgrammingError

class Command(BaseCommand):
    help = "Create a superuser automatically"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = "David"
        email = "david@gmail.com"
        password = "Official@lasop1"

        try:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully!"))
            else:
                self.stdout.write(self.style.WARNING(f"Superuser '{username}' already exists."))
        except (OperationalError, ProgrammingError) as e:
            self.stderr.write(self.style.ERROR(f"Database not ready: {e}"))
