from rest_framework.pagination import PageNumberPagination


class FivePagination(PageNumberPagination):
    """Пагинация для вывода 5 моделей на 1 странице"""
    page_size = 5