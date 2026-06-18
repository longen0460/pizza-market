from django.contrib import admin
from .models import Category, Pizza, Drink, Snack, SideDish

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'ordering']
    list_editable = ['is_active', 'ordering']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'is_available']
    list_display_links = ['name']
    list_editable = ['price', 'is_available']
    list_filter = ['category', 'is_available', 'created_at']
    search_fields = ['name', 'description']

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'volume', 'price', 'is_available']
    list_display_links = ['name']
    list_editable = ['volume', 'price', 'is_available']
    list_filter = ['category', 'volume', 'is_available']
    search_fields = ['name', 'description']

@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'is_available']
    list_display_links = ['name']
    list_editable = ['price', 'is_available']
    list_filter = ['category', 'is_available']
    search_fields = ['name', 'description']

@admin.register(SideDish)
class SideDishAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'is_available']
    list_display_links = ['name']
    list_editable = ['price', 'is_available']
    list_filter = ['category', 'is_available']
    search_fields = ['name', 'description']