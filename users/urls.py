from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateApiView, AppendToBasketView, DeleteFromBasketView, BasketRetrieveView, \
    BasketDestroyAPIView

app_name = UsersConfig.name


urlpatterns = [
    # Урлы для пользователей
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreateApiView.as_view(), name='register'),

    # Урлы для корзины
    path('append/<int:product_id>/', AppendToBasketView.as_view(), name='basket-append'),
    path('delete/<int:product_id>/', DeleteFromBasketView.as_view(), name='basket-delete'),
    path('basket/', BasketRetrieveView.as_view(), name='view-retrieve'),
    path('<int:pk>/destroy/', BasketDestroyAPIView.as_view(), name='basket-destroy'),
]