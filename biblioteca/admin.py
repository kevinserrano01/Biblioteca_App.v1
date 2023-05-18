from django.contrib import admin
from biblioteca.models import PrestamoLibro

# Tarea de Kev
class PrestamoLibroAdmin(admin.ModelAdmin):
    model = PrestamoLibro
    list_display = ("id", "fecha_prestamos", "fecha_devolucion", "socio", "empleado", "libro")
    list_search = ("socio", "libro", "empleado")




admin.site.register(PrestamoLibro, PrestamoLibroAdmin)