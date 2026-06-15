from django.contrib import admin
from .models import Pizza

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_available', 'id']
    list_editable = ['price', 'is_available']
    list_filter = ['is_available']
    search_fields = ['name']
    
    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'