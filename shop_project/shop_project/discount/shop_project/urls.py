from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from discount.views import DiscountViewSet  # Импорт вашего ViewSet

router = DefaultRouter()
router.register(r'discounts', DiscountViewSet)  # Добавляем URL для скидок

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('api/', include(router.urls)),  # API для скидок
]

