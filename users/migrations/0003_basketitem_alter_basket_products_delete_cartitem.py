# Generated by Django 5.1.6 on 2025-02-09 01:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_subcategory'),
        ('users', '0002_basket_cartitem_basket_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Кол-во продукта в корзине')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_basket', to='users.basket', verbose_name='Пользователь')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Продукт в корзине')),
            ],
        ),
        migrations.AlterField(
            model_name='basket',
            name='products',
            field=models.ManyToManyField(through='users.BasketItem', to='products.product'),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
