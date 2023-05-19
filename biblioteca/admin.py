from django.contrib import admin
from biblioteca.models import PrestamoLibro, Libro, Empleado, Socio, Autor

# Tarea de Kevin
class PrestamoLibroAdmin(admin.ModelAdmin):
    model = PrestamoLibro
    list_display = ("id", "fecha_prestamos", "fecha_devolucion", "socio", "empleado", "libro")
    list_search = ("socio", "libro", "empleado")

#Tarea Andrea
class RegistroModeloLibro(admin.ModelAdmin):
    model= Libro 
    list_display=("id", "titulo","descripcion","isbn","autor","activo" )
    list_search= ("titulo","autor")
    list_filter=("titulo","autor","isbn")

# Tarea de Luis
class AutorAdmin(admin.ModelAdmin):
    model = Autor
    list_display = ("id", "nombre", "apellido", "nacionalidad", "activo")
    list_search = ("nombre", "apellido")
    list_filter = ("activo", "nacionalidad")

# Tarea de Naira
class EmpleadoAdmin(admin.ModelAdmin):
    model=Empleado
    list_display=("id","nombre","apellido","activo")
    search_fields=("nombre",)
    list_filter=("activo",)

# tarea de Gustavo
class SocioAdmin(admin.ModelAdmin):
    model=Socio
    list_display=("id","nombre","apellido","activo")
    search_fields=("nombre", "apellido")
    list_filter=("activo",)

admin.site.register(Socio, SocioAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, RegistroModeloLibro)
admin.site.register(PrestamoLibro, PrestamoLibroAdmin)
admin.site.register(Empleado, EmpleadoAdmin)