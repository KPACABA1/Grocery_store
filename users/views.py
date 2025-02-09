from django.db import transaction
from django.db.models import F
from rest_framework import status, serializers
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response

from products.models import Product
from users.models import User, Basket, BasketItem
from users.serializers import UserSerializer, BasketSerializer


class UserCreateApiView(CreateAPIView):
    """Класс для регистрации пользователя."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Вмешиваюсь в логику сериализатора, чтобы более безопасно создать пользователя."""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class AppendToBasketView(CreateAPIView):
    """Класс для добавления продукта в корзину."""
    serializer_class = BasketSerializer

    # Обеспечиваем атомарность операции
    @transaction.atomic
    def perform_create(self, serializer):
        """Метод для добавления товара в корзину."""
        # Получили номер продукта, корзину пользователя и сам продукт
        product_id = self.kwargs.get('product_id')
        print(self.request.user)
        basket, created = Basket.objects.get_or_create(user=self.request.user)
        product = Product.objects.filter(id=product_id).first()

        # Если пользователь ввёл ошибочный номер продукта вызываем ошибку
        if not product:
            raise serializers.ValidationError({"error": "Такого продукта не существует"})

        # Создаю у пользователя данный товар в корзине, если он уже там есть, то прибавляю к нему +1
        basket_item, created = BasketItem.objects.get_or_create(basket=basket, product=product)
        if not created:
            basket_item.quantity = F('quantity') + 1
            basket_item.save()

        # Возвращаю обновленную корзину
        serializer.instance = basket


class DeleteFromBasketView(DestroyAPIView):
    """Класс для удаления товара из корзины."""
    serializer_class = BasketSerializer

    # Обеспечиваем атомарность операции
    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        """Метод для удаления товара из корзины"""
        # Получаем номер продукта
        product_id = self.kwargs.get('product_id')

        # Проверили что у пользователя вообще есть корзина
        basket = Basket.objects.prefetch_related('items_basket__product').get_or_create(user=self.request.user)
        # Проверили что у пользователя есть именно этот продукт в корзине
        try:
            basket_item = BasketItem.objects.get(basket=basket[0].id, product_id=product_id)
        except:
            raise serializers.ValidationError({"error": "Такого продукта в корзине нет"})

        # Если количество товара больше 1, уменьшаем его
        if basket_item.quantity > 1:
            basket_item.quantity = F('quantity') - 1  # Атомарное уменьшение количества
            basket_item.save()
        else:
            # Если количество равно 1, удаляем товар из корзины
            basket_item.delete()

        # Возвращаем сообщение об успехе
        return Response({"message": "Успешно"}, status=status.HTTP_200_OK)


class BasketRetrieveView(RetrieveAPIView):
    """Класс показывает корзину текущего пользователя"""
    serializer_class = BasketSerializer

    def get_object(self):
        """Метод показывает корзину текущего пользователя."""
        basket, created = Basket.objects.prefetch_related('items_basket__product').get_or_create(user=self.request.user)
        return basket


class BasketDestroyAPIView(DestroyAPIView):
    """Класс для полной очистки корзины"""
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
