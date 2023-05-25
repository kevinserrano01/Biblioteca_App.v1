from django.urls import path
from . import views

urlpatterns = [
    path('empleados/desactivar/<int:empleado_id>', views.desactivar_Registro_Empleado, name='desactivar_Registro_Empleado'),
    path('empleados/listado/', views.listado_empleados, name="listado_empleados"),
    path('empleados/crear_empleado/', views.nuevo_empleado, name='nuevo_empleado'),
    path('actualizar_empleado/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/activar/<int:empleado_id>', views.activar_Registro_Empleado, name='activar_Registro_Empleado'),
    path('socios/listado', views.listado_socios, name="listado_socios"),
]