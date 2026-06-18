from django.shortcuts import render
from .models import Category, Pizza, Drink, Snack, SideDish

def menu_view(request):
    categories = Category.objects.filter(is_active=True).prefetch_related(
        'pizzas',
        'drinks',
        'snacks',
        'side_dishes'
    )
    
    context = {
        'categories': categories,
    }
    return render(request, 'menu/menu.html', context)