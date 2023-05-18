from django.db import models



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