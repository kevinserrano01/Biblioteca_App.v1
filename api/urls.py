from django.urls import path
from . import views

urlpatterns = [
    path('libros/',
         views.listado_libros, 
         name='listado_libros'
    ),
    path('libros/<int:libro_id>',views.detalle_libro, name='detalle_libro'),
]