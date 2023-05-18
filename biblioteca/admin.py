from django.contrib import admin
from biblioteca.models import Autor,Libro ##
# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    model=Libro
    list_display=("id","titulo","descripcion","isbn","autor","activo")
    search_fields=("titulo","autor__nombre")
    list_filter=("autor__nombre",)


admin.site.register(Libro, LibroAdmin) ##
