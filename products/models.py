from django.db import models


class Category(models.Model):
    """Модель категории."""
    name = models.CharField(max_length=50, verbose_name='Название', unique=True)
    slug = models.CharField(max_length=50, verbose_name='slug', unique=True)
    picture = models.ImageField(upload_to='category_picture/', blank=True, null=True,
                                verbose_name='Изображение')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Subcategory(models.Model):
    """Модель подкатегории."""
    name = models.CharField(max_length=50, verbose_name='Название', unique=True)
    slug = models.CharField(max_length=50, verbose_name='slug', unique=True)
    picture = models.ImageField(upload_to='subcategory_picture/', blank=True, null=True,
                                verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория',
                                 related_name='subcategory_category', null=True, blank=True)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    """Модель продукта."""
    name = models.CharField(max_length=50, verbose_name='Название', unique=True)
    slug = models.CharField(max_length=50, verbose_name='slug', unique=True)
    picture = models.ImageField(upload_to='products_picture/', blank=True, null=True,
                                verbose_name='Изображение')
    price = models.PositiveIntegerField(verbose_name='Цена')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория',
                                 related_name='product_subcategory', null=True, blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name}'
