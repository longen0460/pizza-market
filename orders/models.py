from django.db import models
from django.conf import settings
from menu.models import Pizza

class Order(models.Model):
    # Варианты статусов для заказа (как выпадающий список)
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),    # (значение в БД, человеческое название)
        ('cooking', 'Готовится'),
        ('delivery', 'Доставка'),
        ('completed', 'Доставлен'),
    ]
    
    # Внешний ключ к пользователю (чей это заказ)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Поля для оформления заказа
    name = models.CharField(max_length=100, verbose_name="Имя")
    address = models.TextField(verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    
    # Выбор статуса из списка выше
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Общая стоимость заказа
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Дата создания (автоматически)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Заказ #{self.id} - {self.name}"

class OrderItem(models.Model):
    # К какому заказу относится товар
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    # Какая пицца
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    
    # Количество
    quantity = models.PositiveIntegerField()
    
    # Цена на момент покупки (сохраняем, чтобы цена не менялась)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.pizza.name} x{self.quantity}"