from django.db import models
from django.forms import ImageField

# Create your models here.
class Producto(models.Model):

    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos',blank=True,null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre