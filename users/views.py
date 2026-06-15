from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from orders.models import Order

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('menu')
    else:
        form = RegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'users/profile.html', {'orders': orders})

# ДОБАВЛЯЕМ ЭТУ ФУНКЦИЮ ДЛЯ ВЫХОДА
def custom_logout(request):
    logout(request)
    return render(request, 'users/logged_out.html')