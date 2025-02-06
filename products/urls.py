from django.urls import path

from products.apps import ProductsConfig
from products.views import CategoryListAPIView

app_name = ProductsConfig.name

urlpatterns = [
    # Урлы для модели категорий
    path('category_list/', CategoryListAPIView.as_view(), name='category-list'),
]