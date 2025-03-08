import environ
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

env = environ.Env()
environ.Env.read_env()  # Load environment variables from .env

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()
        
        username = env("DJANGO_SUPERUSER_USERNAME", default=None)
        email = env("DJANGO_SUPERUSER_EMAIL", default=None)
        password = env("DJANGO_SUPERUSER_PASSWORD", default=None)

        if not username or not email or not password:
            self.stdout.write(self.style.ERROR("Superuser credentials are missing in .env!"))
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully!"))
        else:
            self.stdout.write(self.style.WARNING(f"Superuser '{username}' already exists."))
