from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index,name='index'),  #primer cambio   
    path('/empleados/desactivar/<int:id>', views.desactivar_Registro_Empleado, name='desactivar_Registro_Empleado'),
]