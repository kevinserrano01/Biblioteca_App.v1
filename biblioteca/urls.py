from django.urls import path
from . import views

urlpatterns = [
    path('empleados/desactivar/<int:id>', views.desactivar_Registro_Empleado, name='desactivar_Registro_Empleado'),
    path('empleados/listado/', views.listado_empleados, name="listado_empleados"),
    path('actualizar_empleado/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/activar/<int:id>', views.activar_Registro_Empleado, name='activar_Registro_Empleado'),
]