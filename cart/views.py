from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from .models import Cart, CartItem
from menu.models import Pizza, Drink, Snack, SideDish

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    total = sum(item.content_object.price * item.quantity for item in items)
    return render(request, 'cart/cart.html', {'items': items, 'total': total})

@login_required
def add_to_cart(request, model_type, item_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    models = {
        'pizza': Pizza,
        'drink': Drink,
        'snack': Snack,
        'side': SideDish,
    }
    
    model = models.get(model_type)
    if not model:
        return redirect('menu')
    
    product = get_object_or_404(model, id=item_id, is_available=True)
    
    content_type = ContentType.objects.get_for_model(product)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        content_type=content_type,
        object_id=product.id,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'✅ Количество товара "{product.name}" увеличено!')
    else:
        messages.success(request, f'✅ Товар "{product.name}" добавлен в корзину!')
    
    return redirect('cart')