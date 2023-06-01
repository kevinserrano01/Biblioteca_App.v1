from django.shortcuts import render
from biblioteca.models import Libro
from django.http import JsonResponse

#Nai
def listado_libros(request):
    libros = list(map(lambda libro: libro.pop('descripcion'), Libro.objects.values())) #lista de libros sin su descripcion
    return JsonResponse(libros, safe=False)