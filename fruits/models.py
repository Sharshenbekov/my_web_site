from django.db import models


class Fruits(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фрукт'
        verbose_name_plural = 'Фрукты'


class Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
