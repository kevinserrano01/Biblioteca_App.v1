from django.db import models

# Create your models here.
class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField
    activo = models.BooleanField(default= True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
