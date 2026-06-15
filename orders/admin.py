from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'total_price', 'status', 'created_at']
    list_editable = ['status']
    list_filter = ['status', 'created_at']
    search_fields = ['name', 'phone', 'address']
    inlines = [OrderItemInline]
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'