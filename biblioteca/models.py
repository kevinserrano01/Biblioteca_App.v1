from django.db import models

# Create your models here.

class Autor(models.Model):
    pass

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

