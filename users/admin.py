from django.contrib import admin

from users.models import Basket, BasketItem, User


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    """Админка для корзины."""
    list_display = ('id', 'user')


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    """Админка для хз чего."""
    list_display = ('id', 'basket', 'product')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка для пользователей."""
    list_display = ('id',)
