from django.contrib import admin
from biblioteca.models import PrestamoLibro, Libro, Empleado, Socio

#Tarea Andy
class RegistroModeloLibro(admin.ModelAdmin):
    model= Libro 
    list_display=("id", "titulo","descripcion","isbn","autor","activo" )
    list_search= ("titulo","autor")
    list_filter=("titulo","autor","isbn")

class EmpleadoAdmin(admin.ModelAdmin):
    model=Empleado
    list_display=("id","nombre","apellido","activo")
    search_fields=("nombre",)
    list_filter=("activo",)

class SocioAdmin(admin.ModelAdmin):
    model=Socio
    list_display=("id","nombre","apellido","activo")
    search_fields=("nombre", "apellido")
    list_filter=("activo",)

class PrestamoLibroAdmin(admin.ModelAdmin):
    model = PrestamoLibro
    list_display=("nombre",)
    search_fields=("socio", "libro", "empleado",)

admin.site.register(Socio, SocioAdmin)
admin.site.register(Libro, RegistroModeloLibro)
admin.site.register(PrestamoLibro, PrestamoLibroAdmin)
admin.site.register(Empleado, EmpleadoAdmin)