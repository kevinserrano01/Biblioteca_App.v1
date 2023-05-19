from django.contrib import admin
from biblioteca.models import PrestamoLibro, Autor

# Tarea de Kev
class PrestamoLibroAdmin(admin.ModelAdmin):
    model = PrestamoLibro
    list_display = ("id", "fecha_prestamos", "fecha_devolucion", "socio", "empleado", "libro")
    list_search = ("socio", "libro", "empleado")



admin.site.register(PrestamoLibro, PrestamoLibroAdmin)

# Tarea de Luis
class AutorAdmin(admin.ModelAdmin):
    model = Autor
    list_display = ("id", "nombre", "apellido", "nacionalidad", "activo")
    list_search = ("nombre", "apellido")
    list_filter = ("activo", "nacionalidad")
    


admin.site.register(Autor, AutorAdmin)