from django.db import models

# Create your models here.
class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField
    activo = models.BooleanField(default= True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# Tarea de Kev
class PrestamoLibro(models.Model):
    fecha_prestamos = models.DateField()
    fecha_devolucion = models.DateField()
    socio = models.ForeignKey(
        Socio,
        on_delete=models.CASCADE
    )
    empleado: models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE
    )
    libro: models.ForeignKey(
        Libro,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.fecha_prestamos} - {self.fecha_devolucion}'
