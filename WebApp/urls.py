from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('biblioteca.urls')),
    path('admin/', admin.site.urls), # user: admin - password: admin123
    path('biblioteca/', include('biblioteca.urls')),
    path('', include('biblioteca.urls')),
    path('api/', include('api.urls')),
]

# Tarjeta SC3S2-76 creada por adelantado necesaria para archivos estaticos - Nai
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)