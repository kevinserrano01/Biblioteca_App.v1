from django.contrib import admin
from biblioteca.models import Empleado, Socio
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    model=Empleado
    list_display=("id","nombre","apellido","activo")
    search_fields=("nombre",)
    list_filter=("activo",)

class EmpleadoAdmin(admin.ModelAdmin):
    model=Empleado
    list_display=("id","nombre","apellido","activo")
    search_fields=("nombre",)
    list_filter=("activo",)
    


admin.site.register(Empleado, EmpleadoAdmin)

class SocioAdmin(admin.ModelAdmin):
    model=Socio
    list_display=("id","nombre","apellido","activo")
    search_fields=("nombre", "apellido")
    list_filter=("activo",)
    


admin.site.register(Socio, SocioAdmin)
