from django.shortcuts import render
from django.http import JsonResponse
from biblioteca.models import Libro
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.shortcuts import render
from biblioteca.models import Libro
from django.http import JsonResponse
from django.db.models import F, Value
from django.db.models.functions import Concat

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro,id=libro_id)
    libro_dict=model_to_dict(libro)
    return JsonResponse(libro_dict, safe=False)

def listado_libros(request):
    libros = Libro.objects.annotate(autor_nombre_completo=Concat(F('autor_nombre'), Value(' '), F('autor_apellido')))
    libros = libros.values('id', 'titulo', autor_=F('autor_nombre_completo'))
    return JsonResponse(list(libros), safe=False)

