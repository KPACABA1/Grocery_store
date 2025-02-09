from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from products.serializers import ProductSerializer
from users.models import User, Basket, BasketItem


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователей."""
    class Meta:
        model = User
        fields = "__all__"


class BasketItemSerializer(serializers.ModelSerializer):
    """Сериализатор для модели продуктов в корзине."""
    product = ProductSerializer()

    class Meta:
        model = BasketItem
        fields = ('id', 'basket', 'product', 'quantity')


class BasketSerializer(serializers.ModelSerializer):
    """Сериализатор для модели корзины."""
    # Поле вывода состава корзины
    items_basket = BasketItemSerializer(many=True, read_only=True)

    # Поле подсчета количества товаров
    number_products = SerializerMethodField()
    def get_number_products(self, basket):
        quantity = 0
        for number_product in BasketItem.objects.filter(basket=basket):
            quantity += number_product.quantity
        return quantity

    # Поле итоговой стоимости всех продуктов в корзине
    cost_of_all_products = SerializerMethodField()
    def get_cost_of_all_products(self, basket):
        cost = 0
        for number_product in BasketItem.objects.filter(basket=basket):
            cost += (number_product.product.price * number_product.quantity)
        return cost

    class Meta:
        model = Basket
        fields = ('items_basket', 'number_products', 'cost_of_all_products')
