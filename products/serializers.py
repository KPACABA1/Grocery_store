from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from products.models import Category, Subcategory, Product


class SubcategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели подкатегорий."""
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'slug', 'picture']


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели категорий."""
    # Настройка поля вывода подкатегорий у категории
    subcategory_category = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id','name', 'slug', 'picture', 'subcategory_category']


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели продуктов."""
    # Получаю поля названий категорий и подкатегорий
    subcategory = SerializerMethodField()
    category = SerializerMethodField()

    # Методы для получения этих полей
    def get_subcategory(self, product):
        return product.subcategory.name

    def get_category(self, product):
        return product.subcategory.category.name



    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'picture', 'price', 'subcategory', 'category']
