from django.db import models
from django.contrib.auth.models import AbstractUser

# AbstractUser - расширяем стандартного пользователя Django
class User(AbstractUser):
    # Добавляем дополнительные поля к стандартному пользователю
    # blank=True - поле не обязательно для заполнения
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    address = models.TextField(blank=True, verbose_name="Адрес")
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"