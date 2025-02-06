from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Модель пользователя."""
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}'

