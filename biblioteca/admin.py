from django.contrib import admin
from biblioteca.models import Empleado
# Register your models here.


class EmpleadoAdmin(admin.ModelAdmin):
    model=Empleado
    list_display=("id","nombre","apellido","activo")
    search_fields=("nombre",)
    list_filter=("activo",)
    


admin.site.register(Empleado, EmpleadoAdmin)

