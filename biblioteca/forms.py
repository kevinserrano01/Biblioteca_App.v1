from django import forms
from biblioteca.models import Autor, Empleado, Socio

class CrearNuevoEmpleado(forms.Form): # Kev
    nombre = forms.CharField(label='Nombre del empleado', max_length=200)
    apellido = forms.CharField(label='Apellido del empleado', max_length=200)
    nro_legajo = forms.CharField(label='Numero de legajo', max_length=200)

class ActualizarAutor(forms.Form): # Kev
    class Meta:
        model = Autor
        fields = ('__all__') # Editar todos sus caracteristicas

class ActualizarSocio(forms.Form): # Kev
    class Meta:
        model = Socio
        fields = ('__all__')