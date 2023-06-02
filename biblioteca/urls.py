from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
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
    path('autores/activar/<int:autor_id>/', views.activar_registro_autor, name='activar_registro_autor'),
    path('socios/desactivar/<int:socio_id>/', views.desactivar_registro_socio, name='desactivar_registro_socio'),
    path('autores/nuevo/', views.reg_nuevAutores, name='nuevos_Autores'),
    path('socios/nuevo/', views.reg_nuevSocios, name='nuevos_Socios'),
    path('socios/modificar/<int:socio_id>', views.actualizar_socios, name='actualizar_socios'),
    path('libro/nuevo/', views.nuevo_libro, name='nuevo_libro'),
    path('prestamos/modificar/<int:prestamoLibro_id>', views.actualizar_Prestamo_Libro, name='actualizar_prestamo_libro'),
    path('prestamos/eliminar/<int:prestamoLibro_id>', views.eliminar_regPrestamo, name='eliminar_reg_prestamo_libro'),
    path('socios/actualizar/<int:socio_id>', views.actualizar_socios, name='actualizar_socio'),
    path('libros/activar/<int:libro_id>', views.activar_registro_libro, name='activar_registro_libro'),
    path('prestamos/listado/', views.listado_prestamolibro, name='listado_prestamolibro'),
    path('prestamos/nuevo/', views.nuevo_prestamo_libro, name='nuevo_prestamo_libros'),
    path('prestamos/modificar/<int:prestamoLibro_id>', views.actualizar_Prestamo_Libro, name='actualizar_prestamo_libro'),
    
]

















