from django.urls import path
from . import views

urlpatterns = [
    path('empleados/desactivar/<int:empleado_id>', views.desactivar_Registro_Empleado, name='desactivar_Registro_Empleado'),
    path('empleados/listado/', views.listado_empleados, name="listado_empleados"),
    path('empleados/crear_empleado/', views.nuevo_empleado, name='nuevo_empleado'),
    path('actualizar_empleado/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/activar/<int:empleado_id>', views.activar_Registro_Empleado, name='activar_Registro_Empleado'),
    path('autores/listado/', views.listado_autores, name='listado_autores'),
    path('socios/activar/<int:socio_id>', views.activar_Registro_Socio, name='activar_Registro_Socio'),
    path('autores/desactivar/<int:autor_id>', views.desactivar_Registro_Autor, name='desactivar_Registro_Autor'),
    path('socios/listado/', views.listado_socios, name="listado_socios"),
    path('autores/modificar/<int:autor_id>', views.actualizar_autor, name='actualizar_autor'),
]