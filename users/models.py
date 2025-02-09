from django.contrib.auth.models import AbstractUser
from django.db import models

from products.models import Product


class User(AbstractUser):
    """Модель пользователя."""
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}'


class Basket(models.Model):
    """Модель корзины."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='basket_user', verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f"корзина {self.user.username}"


class BasketItem(models.Model):
    """Модель продукта хранящегося в корзине."""
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='items_basket', verbose_name='Корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт в корзине')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кол-во продукта в корзине')

    class Meta:
        verbose_name = 'Предмет в корзине'
        verbose_name_plural = 'Предметы в корзине'

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.basket}"
