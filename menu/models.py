from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(unique=True, verbose_name="URL-идентификатор")
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name="Изображение")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    ordering = models.IntegerField(default=0, verbose_name="Порядок сортировки")
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['ordering', 'name']
    
    def __str__(self):
        return self.name

class Pizza(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='pizzas', verbose_name="Категория", null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='pizzas/', verbose_name="Изображение")
    is_available = models.BooleanField(default=True, verbose_name="Доступно")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пицца"
        verbose_name_plural = "Пиццы"

class Drink(models.Model):
    VOLUME_CHOICES = [
        (0.33, '0.33 л'),
        (0.5, '0.5 л'),
        (1.0, '1 л'),
        (1.5, '1.5 л'),
        (2.0, '2 л'),
    ]
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='drinks', verbose_name="Категория")
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    volume = models.FloatField(choices=VOLUME_CHOICES, verbose_name="Объем (л)")
    image = models.ImageField(upload_to='drinks/', verbose_name="Изображение")
    is_available = models.BooleanField(default=True, verbose_name="Доступно")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return f"{self.name} ({self.get_volume_display()})"

    class Meta:
        verbose_name = "Напиток"
        verbose_name_plural = "Напитки"
        ordering = ['volume', 'name']

class Snack(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='snacks', verbose_name="Категория")
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='snacks/', verbose_name="Изображение")
    is_available = models.BooleanField(default=True, verbose_name="Доступно")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Закуска"
        verbose_name_plural = "Закуски"

class SideDish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='side_dishes', verbose_name="Категория")
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='side_dishes/', verbose_name="Изображение")
    is_available = models.BooleanField(default=True, verbose_name="Доступно")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Гарнир"
        verbose_name_plural = "Гарниры"
        ordering = ['name']

# Для совместимости с корзиной (указываем, какие модели можно добавлять)
PRODUCT_MODELS = {
    'pizza': Pizza,
    'drink': Drink,
    'snack': Snack,
    'side': SideDish,
}