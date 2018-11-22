from django.db import models

# Create your models here.
class Productos(models.Model):
    name = models.CharField(max_length=200)
    cost = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Productos"

class Categorias(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categorias"