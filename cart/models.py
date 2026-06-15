from django.db import models
from django.conf import settings  # Чтобы получить настройки проекта
from menu.models import Pizza  # Импортируем модель пиццы

class Cart(models.Model):
    # OneToOneField - связь один к одному (у одного пользователя - одна корзина)
    # on_delete=models.CASCADE - если пользователь удалится, удалится и корзина
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # auto_now_add=True - автоматически поставит текущую дату при создании
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Корзина {self.user.username}"

class CartItem(models.Model):
    # ForeignKey - связь многие к одному (в одной корзине много товаров)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    
    # Ссылка на конкретную пиццу
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    
    # PositiveIntegerField - только положительные числа (1, 2, 3...)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.pizza.name} x{self.quantity}"