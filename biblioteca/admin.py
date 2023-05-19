from django.contrib import admin
from biblioteca.models import PrestamoLibro, Libro

#Tarea Andy
class RegistroModeloLibro(admin.ModelAdmin):
    model= Libro 
    list_display=("id", "titulo","descripcion","isbn","autor","activo" )
    list_search= ("titulo","autor")
    list_filter=("titulo","autor","isbn")

# Tarea de Kev
class PrestamoLibroAdmin(admin.ModelAdmin):
    model = PrestamoLibro
    list_display = ("id", "fecha_prestamos", "fecha_devolucion", "socio", "empleado", "libro")
    list_search = ("socio", "libro", "empleado")




admin.site.register(Libro, RegistroModeloLibro)
admin.site.register(PrestamoLibro, PrestamoLibroAdmin)