from django.contrib import admin

from products.models import Category, Subcategory, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админка для категорий."""
    list_display = ('id', 'name')


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    """Админка для подкатегорий."""
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка для продуктов."""
    list_display = ('id', 'name')
