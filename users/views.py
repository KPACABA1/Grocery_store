from rest_framework.generics import CreateAPIView

from users.models import User
from users.serializers import UserSerializer


class UserCreateApiView(CreateAPIView):
    """Класс для регистрации пользователя."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Вмешиваюсь в логику сериализатора, чтобы более безопасно создать пользователя."""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
