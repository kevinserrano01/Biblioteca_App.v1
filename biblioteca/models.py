from django.db import models

# Create your models here.



class Libro(models.Model):
    titulo=models.CharField(max_length=80) #consulta si ponemos longitud
    descripcion=models.CharField(max_length=80) #idem
    isbn=models.IntegerField(default=0) #idem
    autor=models.ForeignKey(
        Autor,
        related_name="libros",
        on_delete=models.CASCADE,
    activo=models.BooleanField(default=True)

    )
    def __str__(self):
        return f"{self.titulo} - {self.autor}"



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
