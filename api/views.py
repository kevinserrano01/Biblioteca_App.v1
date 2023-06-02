from django.shortcuts import render
from django.http import JsonResponse
from biblioteca.models import Libro
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.shortcuts import render
from biblioteca.models import Libro
from django.http import JsonResponse


def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro,id=libro_id)
    libro_dict=model_to_dict(libro)
    return JsonResponse(libro_dict, safe=False)



#Nai
def listado_libros(request):
    libros = list(map(lambda libro: libro.pop('descripcion'), Libro.objects.values())) #lista de libros sin su descripcion
    return JsonResponse(libros, safe=False)
   




####GUS### MUESTRA TODOS LOS LIBROS EN FORMATO JSON
# def listado_libros(request):
#     libros = list(Libro.objects.values())
#     return JsonResponse(libros,safe=False)

