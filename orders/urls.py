from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),           # Оформление заказа
    path('status/<int:order_id>/', views.order_status, name='order_status'),  # Статус заказа
]