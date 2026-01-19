from django.db import models

# Create your models here.
class Menu(models.Model):
    first_food = models.CharField(max_length=240, verbose_name="имя первого блюда")
    food2_name = models.CharField(max_length=240, verbose_name="имя второго блюда")
    dessert = models.IntegerField(verbose_name="десерт")
    adress = models.EmailField(verbose_name="адресс")
    visual = models.ImageField(verbose_name="визуализация")

    def __str__(self):
        return self.first_food
    
