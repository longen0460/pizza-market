from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import Cart, CartItem

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    
    if not items:
        messages.warning(request, 'Ваша корзина пуста!')
        return redirect('cart')
    
    total = sum(item.content_object.price * item.quantity for item in items)
    
    if request.method == 'POST':
        # Создаем заказ
        order = Order.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            address=request.POST.get('address'),
            phone=request.POST.get('phone'),
            total_price=total,
            status='pending'
        )
        
        # Переносим товары из корзины в заказ
        for item in items:
            OrderItem.objects.create(
                order=order,
                product_type=item.content_type.model,  # 'pizza', 'drink', 'snack', 'side'
                product_id=item.object_id,
                product_name=item.content_object.name,
                quantity=item.quantity,
                price=item.content_object.price
            )
        
        # Очищаем корзину
        items.delete()
        
        messages.success(request, f'Заказ #{order.id} успешно оформлен!')
        return redirect('order_status', order_id=order.id)
    
    context = {
        'items': items,
        'total': total,
    }
    return render(request, 'orders/checkout.html', context)

@login_required
def order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/status.html', {'order': order})