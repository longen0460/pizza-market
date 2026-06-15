from django.shortcuts import render
from .models import Pizza

def menu_view(request):
    # Получаем все доступные пиццы из БД
    pizzas = Pizza.objects.filter(is_available=True)
    # Передаем их в шаблон
    return render(request, 'menu/menu.html', {'pizzas': pizzas})