from rest_framework.generics import ListAPIView

from products.models import Category, Product
from products.paginations import FivePagination
from products.serializers import CategorySerializer, ProductSerializer


class CategoryListAPIView(ListAPIView):
    """Класс для вывода всех моделей категорий."""
    # Используя prefetch_related программа избегает проблемы "N+1 запросов". Это гарантирует, что все подкатегории будут
    # загружены за один запрос, а не по отдельному запросу для каждой категории. И сделал чтобы выводились все по
    # порядку
    queryset = Category.objects.prefetch_related('subcategory_category').order_by('id')
    serializer_class = CategorySerializer
    pagination_class = FivePagination


class ProductListAPIView(ListAPIView):
    """Класс для вывода всех моделей продуктов."""
    # Используя prefetch_related программа избегает проблемы "N+1 запросов". Это гарантирует, что все подкатегории будут
    # загружены за один запрос, а не по отдельному запросу для каждой категории. И сделал чтобы выводились все по
    # порядку
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = FivePagination
