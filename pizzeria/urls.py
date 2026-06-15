from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),        # Главная страница (меню)
    path('cart/', include('cart.urls')),   # Все URL для корзины
    path('orders/', include('orders.urls')), # Все URL для заказов
    path('users/', include('users.urls')),   # Все URL для пользователей
]

# ЭТО ВАЖНО: Добавляем поддержку загрузки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)