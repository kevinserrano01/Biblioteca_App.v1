from django import forms
from biblioteca.models import Autor, Empleado, Socio

class CrearNuevoEmpleado(forms.Form): # Kev
    nombre = forms.CharField(label='Nombre del empleado', max_length=200)
    apellido = forms.CharField(label='Apellido del empleado', max_length=200)
    nro_legajo = forms.CharField(label='Numero de legajo', max_length=200)

class ActualizarAutor(forms.ModelForm): # Kev
    class Meta:
        model = Autor
        fields = ('__all__') # Editar todos sus caracteristicas

class ActualizarSocio(forms.Form): # Kev
    class Meta:
        model = Socio
        fields = ('nombre','apellido')


class CrearNuevoAutor(forms.Form):
    nombre = forms.CharField(label='Nombre del autor', max_length=200)
    apellido = forms.CharField(label='Apellido del autor', max_length=200)
    nacionalidad = forms.CharField(label='Nacionalidad', max_length=200)


class CrearNuevoSocio(forms.Form):
    nombre = forms.CharField(label='Nombre del socio', max_length=50)
    apellido = forms.CharField(label='Apellido del socio', max_length=50)
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento')