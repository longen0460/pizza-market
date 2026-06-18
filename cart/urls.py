from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/<str:model_type>/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
]