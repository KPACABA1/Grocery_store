from rest_framework.generics import ListAPIView

from products.models import Category
from products.paginations import CategoryPagination
from products.serializers import CategorySerializer


class CategoryListAPIView(ListAPIView):
    """Класс для вывода всех моделей категорий."""
    # Используя prefetch_related программа избегает проблемы "N+1 запросов". Это гарантирует, что все подкатегории будут
    # загружены за один запрос, а не по отдельному запросу для каждой категории. И сделал чтобы выводились все по
    # порядку
    queryset = Category.objects.prefetch_related('subcategory_category').order_by('id')
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
