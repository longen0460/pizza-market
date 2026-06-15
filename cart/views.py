from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from menu.models import Pizza

@login_required  # Требуем, чтобы пользователь был авторизован
def cart_view(request):
    # Получаем или создаем корзину для текущего пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)
    # Получаем все товары в корзине
    items = CartItem.objects.filter(cart=cart)
    # Считаем общую сумму
    total = sum(item.pizza.price * item.quantity for item in items)
    return render(request, 'cart/cart.html', {'items': items, 'total': total})

@login_required
def add_to_cart(request, pizza_id):
    # Получаем корзину пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)
    # Находим пиццу по ID
    pizza = get_object_or_404(Pizza, id=pizza_id)
    # Пытаемся найти этот товар в корзине
    cart_item, created = CartItem.objects.get_or_create(cart=cart, pizza=pizza)
    
    # Если товар уже был в корзине, увеличиваем количество на 1
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    # Возвращаемся на страницу с меню
    return redirect('menu')