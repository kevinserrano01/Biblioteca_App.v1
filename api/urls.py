from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.listado_libros, name='listado_libros')
]