from rest_framework import serializers

from products.models import Category, Subcategory


class SubcategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели подкатегорий"""
    class Meta:
        model = Subcategory
        fields = ['name', 'slug', 'picture']


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели категорий"""
    # Настройка для вывода всех подкатегорий
    subcategory_category = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id','name', 'slug', 'picture', 'subcategory_category']
