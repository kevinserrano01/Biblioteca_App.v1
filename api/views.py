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
    try:
        libro = Libro.objects.get(id=libro_id)
        libro_dict = {
            'id': libro.id,
            'titulo': libro.titulo,
            'descripcion': libro.descripcion,
            'autor': str(libro.autor)  
        }
        return JsonResponse(libro_dict, safe=False)
    except Libro.DoesNotExist:
        return JsonResponse([], safe=False)
    
def listado_libros(request):
    libros = Libro.objects.all()
    libros_dict = [
        {
            'id': libro.id,
            'titulo': libro.titulo,
            'autor': str(libro.autor) 
        }
        for libro in libros
    ]
    return JsonResponse(libros_dict,safe=False)