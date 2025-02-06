from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),

    # Урлы приложения products
    path('product/', include('products.urls', namespace='product')),

    # # Урлы приложения staff
    # path('staff/', include('staff.urls', namespace='staff')),
]
