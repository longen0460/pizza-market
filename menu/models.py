from django.db import models

class Pizza(models.Model):
    # CharField - для короткого текста (максимум 100 символов)
    # verbose_name - как это поле будет называться в админке
    name = models.CharField(max_length=100, verbose_name="Название")
    
    # TextField - для длинного текста (без ограничения)
    description = models.TextField(verbose_name="Описание")
    
    # DecimalField - для денег (8 цифр всего, 2 после запятой)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    
    # ImageField - для загрузки картинок
    # upload_to='pizzas/' - картинки будут сохраняться в media/pizzas/
    image = models.ImageField(upload_to='pizzas/', verbose_name="Изображение")
    
    # BooleanField - True/False (доступна пицца или нет)
    is_available = models.BooleanField(default=True, verbose_name="Доступно")

    # Это метод, который возвращает название пиццы (для отображения в админке)
    def __str__(self):
        return self.name

    class Meta:
        # Настройки модели
        verbose_name = "Пицца"  # Как будет называться в единственном числе
        verbose_name_plural = "Пиццы"  # Как будет называться во множественном числе