from django import forms
from biblioteca.models import Autor, Empleado, Socio, Libro, PrestamoLibro
from datetime import timedelta

#Empleado

class CrearNuevoEmpleado(forms.Form): # Kev
    nombre = forms.CharField(label='Nombre del empleado', max_length=200)
    apellido = forms.CharField(label='Apellido del empleado', max_length=200)
    nro_legajo = forms.CharField(label='Numero de legajo', max_length=200)

#Socios

class CrearNuevoSocio(forms.Form):
    nombre = forms.CharField(label='Nombre del autor', max_length=50)
    apellido = forms.CharField(label='Apellido del autor', max_length=50)
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento (YYYY-MM-DD)')
class ActualizarSocio(forms.ModelForm): # Kev
    class Meta:
        model = Socio
        fields = ('__all__')

#Autor

class CrearNuevoAutor(forms.Form):
    nombre = forms.CharField(label='Nombre del autor', max_length=200)
    apellido = forms.CharField(label='Apellido del autor', max_length=200)
    nacionalidad = forms.CharField(label='Nacionalidad', max_length=200)
class ActualizarAutor(forms.ModelForm): # Kev
    class Meta:
        model = Autor
        fields = ('__all__') # Editar todos sus caracteristicas

#Libro

class CrearNuevoLibro(forms.Form): #Andrea
  titulo = forms.CharField(label='Nombre del Titulo', max_length=50)
  descripcion = forms.CharField(label='Descripcion', max_length=500)
  isbn=forms.IntegerField(label='ISBN')
  autor = forms.ModelChoiceField(label='Autor', queryset=Autor.objects.filter(activo=True))
class ActualizarLibro(forms.ModelForm): # Nai
    #autores = forms.ModelChoiceField(label='Autor', queryset=Autor.objects.filter(activo=True))
    class Meta:
        model = Libro
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['socio'].queryset = self.fields['socio'].queryset.filter(activo=True)
        self.fields['empleado'].queryset = self.fields['empleado'].queryset.filter(activo=True)
        self.fields['libro'].queryset = self.fields['libro'].queryset.filter(activo=True)

        
class CrearNuevoPrestamo(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['autor'].queryset = self.fields['autor'].queryset.filter(activo=True)

#Prestamo

class CrearNuevoPrestamo(forms.Form): 
    fecha_prestamos = forms.DateField(
        label='Fecha Prestamo (YYYY-MM-DD)'
    )
    #fecha_devolucion=forms.DateField(label='Fecha Devolucion (YYYY-MM-DD)')
    socio = forms.ModelChoiceField(label='Socio', queryset=Socio.objects.filter(activo=True))
    empleado = forms.ModelChoiceField(label='Empleado', queryset=Empleado.objects.filter(activo=True))
    libro = forms.ModelChoiceField(label='Libro', queryset=Libro.objects.filter(activo=True))
      
class ActualizarLibro(forms.ModelForm): #Nai
    #autores = forms.ModelChoiceField(label='Autor', queryset=Autor.objects.filter(activo=True))

class ActualizarPrestamo(forms.ModelForm): #Andrea
    class Meta:
        model = Libro
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['autor'].queryset = self.fields['autor'].queryset.filter(activo=True)
        model=PrestamoLibro
        fields=('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['socio'].queryset = self.fields['socio'].queryset.filter(activo=True)
        self.fields['empleado'].queryset = self.fields['empleado'].queryset.filter(activo=True)
        self.fields['libro'].queryset = self.fields['libro'].queryset.filter(activo=True)





    

    
