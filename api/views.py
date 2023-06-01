from django.shortcuts import render
from django.http import JsonResponse
from biblioteca.models import Libro
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict


def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro,id=libro_id)
    libro_dict = model_to_dict(libro)
    return JsonResponse(libro_dict, safe=False)