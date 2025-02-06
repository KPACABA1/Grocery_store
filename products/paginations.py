from rest_framework.pagination import PageNumberPagination


class CategoryPagination(PageNumberPagination):
    """Пагинация для моделей категорий"""
    page_size = 5