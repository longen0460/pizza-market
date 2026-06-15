from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.models import Cart, CartItem

@login_required
def checkout(request):
    # Получаем корзину пользователя
    cart = Cart.objects.get(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    
    # Если корзина пуста - перенаправляем в меню
    if not items:
        return redirect('menu')
    
    total = sum(item.pizza.price * item.quantity for item in items)
    
    if request.method == 'POST':
        # Создаем новый заказ
        order = Order.objects.create(
            user=request.user,
            name=request.POST['name'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            total_price=total
        )
        
        # Переносим товары из корзины в заказ
        for item in items:
            OrderItem.objects.create(
                order=order,
                pizza=item.pizza,
                quantity=item.quantity,
                price=item.pizza.price
            )
        
        # Очищаем корзину
        items.delete()
        
        # Переходим на страницу статуса заказа
        return redirect('order_status', order_id=order.id)
    
    return render(request, 'orders/checkout.html', {
        'items': items,
        'total': total
    })

@login_required
def order_status(request, order_id):
    # Находим заказ и проверяем, что он принадлежит текущему пользователю
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/status.html', {'order': order})