from django import forms
from biblioteca.models import Empleado

class CrearNuevoEmpleado(forms.ModelForm):
    nombre = forms.CharField(label='Nombre del empleado', max_length=200)
    apellido = forms.CharField(label='Apellido del empleado', max_length=200)
    nro_legajo = forms.CharField(label='Numero de legajo', max_length=200)