from django.urls import path
from . import views

urlpatterns = [
       path('libros/<int:libro_id>',views.detalle_libro, name='detalle_libro'),
]