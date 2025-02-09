from rest_framework import permissions


class BasketOwner(permissions.BasePermission):
    """Проверка на то, что удаляющий корзину пользователь является её владельцем"""
    def has_object_permission(self, request, view, obj):
        if obj.user ==request.user:
            return True
        return False