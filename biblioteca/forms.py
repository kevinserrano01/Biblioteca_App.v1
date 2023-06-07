from django import forms
from biblioteca.models import Autor, Empleado, Socio, Libro, PrestamoLibro
from datetime import timedelta


class CrearNuevoEmpleado(forms.Form): # Kev
    nombre = forms.CharField(label='Nombre del empleado', max_length=200)
    apellido = forms.CharField(label='Apellido del empleado', max_length=200)
    nro_legajo = forms.CharField(label='Numero de legajo', max_length=200)

class CrearNuevoAutor(forms.Form):
    nombre = forms.CharField(label='Nombre del autor', max_length=200)
    apellido = forms.CharField(label='Apellido del autor', max_length=200)
    nacionalidad = forms.CharField(label='Nacionalidad', max_length=200)


class CrearNuevoSocio(forms.Form):
    nombre = forms.CharField(label='Nombre del autor', max_length=50)
    apellido = forms.CharField(label='Apellido del autor', max_length=50)
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento (YYYY-MM-DD)')

class ActualizarAutor(forms.ModelForm): # Kev
    class Meta:
        model = Autor
        fields = ('__all__') # Editar todos sus caracteristicas

class ActualizarSocio(forms.ModelForm): # Kev
    class Meta:
        model = Socio
        fields = ('__all__')


class CrearNuevoAutor(forms.Form):
    nombre = forms.CharField(label='Nombre del autor', max_length=200)
    apellido = forms.CharField(label='Apellido del autor', max_length=200)
    nacionalidad = forms.CharField(label='Nacionalidad', max_length=200)


class CrearNuevoSocio(forms.Form):
    nombre = forms.CharField(label='Nombre del autor', max_length=50)
    apellido = forms.CharField(label='Apellido del autor', max_length=50)
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento (YYYY-MM-DD)')

class CrearNuevoLibro(forms.Form):
  titulo = forms.CharField(label='Nombre del Titulo', max_length=50)
  descripcion = forms.CharField(label='Descripcion', max_length=500)
  isbn=forms.IntegerField(label='ISBN')
  autor = forms.ModelChoiceField(label='Autor', queryset=Autor.objects.filter(activo=True))
  

class ActualizarPrestamo(forms.ModelForm):
    class Meta:
        model=PrestamoLibro
        fields=('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['socio'].queryset = self.fields['socio'].queryset.filter(activo=True)
        self.fields['empleado'].queryset = self.fields['empleado'].queryset.filter(activo=True)
        self.fields['libro'].queryset = self.fields['libro'].queryset.filter(activo=True)

        
class CrearNuevoPrestamo(forms.Form):
    socio = forms.ModelChoiceField(label='Socio', queryset=Socio.objects.filter(activo=True))
    empleado = forms.ModelChoiceField(label='Empleado', queryset=Empleado.objects.filter(activo=True))
    libro = forms.ModelChoiceField(label='Libro', queryset=Libro.objects.filter(activo=True))

# Otra forma de crear un nuevo prestamo es de la siguiente manera:
# class CrearNuevoPrestamo(forms.ModelForm):
    """Lo que hace esto es crear un nuevo prestamo pero con la fecha actual del sistema."""
#     class Meta:
#         model = Empleado
#         fields = '__all__'
        
#     def __init__(self, *args, **kwargs):
#         super(CrearNuevoPrestamo, self).__init__(*args, **kwargs)
#         self.fields['fecha_prestamos'].initial = datetime.now()



'''
def clean_libro(self):
        lista_prestamos =   PrestamoLibro.objects.all()
        for prestamo in lista_prestamos:
            print(prestamo)
'''
    
'''
    from django.core.exceptions import ValidationError
from django.db.models import Q

class PrestamoLibro(models.Model):
    # ...

  def clean(self):
        # Validar que no existan préstamos para el mismo libro en las mismas fechas
        prestamos_existentes = PrestamoLibro.objects.filter(
            libro=self.libro,
            Q(fecha_prestamos_lte=self.fecha_prestamos, fecha_devolucion_gte=self.fecha_prestamos) |
            Q(fecha_prestamos_lte=self.fecha_devolucion, fecha_devolucion_gte=self.fecha_devolucion) |
            Q(fecha_prestamos_gte=self.fecha_prestamos, fecha_devolucion_lte=self.fecha_devolucion)
        ).exclude(pk=self.pk)  # Excluir el préstamo actual si se está editando

        if prestamos_existentes.exists():
            raise ValidationError("El libro ya ha sido prestado en las mismas fechas.")

        # Validar que la fecha de devolución sea posterior a la fecha de préstamo
        if self.fecha_devolucion <= self.fecha_prestamos:
            raise ValidationError("La fecha de devolución debe ser posterior a la fecha de préstamo.")
      '''


class ActualizarLibro(forms.ModelForm): #Nai
    #autores = forms.ModelChoiceField(label='Autor', queryset=Autor.objects.filter(activo=True))
    class Meta:
        model = Libro
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['autor'].queryset = self.fields['autor'].queryset.filter(activo=True)