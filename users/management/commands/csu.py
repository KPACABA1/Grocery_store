from django.core.management import BaseCommand

from users.models import User

# Импортирую данные для имени пользователя админа и пароль
from dotenv import load_dotenv
import os
load_dotenv()


class Command(BaseCommand):
    """Команда для создания админа."""
    def handle(self, *args, **options):
        user = User.objects.create(username=os.getenv('username'))
        user.set_password(os.getenv('POSTGRES_PASSWORD'))
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()