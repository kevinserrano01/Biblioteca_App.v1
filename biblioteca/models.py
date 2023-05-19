from django.db import models

#Tarea Andy
class Empleado(models.Model):
    nombre:models.CharField(max_length=30)
    apellido:models.CharField(max_length=30)
    numero_legajo:models.IntegerField
    activo:models.BooleanField
    
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.numero_legajo} - {self.activo}'

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
    

