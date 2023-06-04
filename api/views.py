from django.http import JsonResponse
from biblioteca.models import Libro
from biblioteca.models import Libro
from django.http import JsonResponse

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