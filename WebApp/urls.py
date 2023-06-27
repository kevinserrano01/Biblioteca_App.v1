from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls), # user: admin - password: admin123
    path('biblioteca/', include('biblioteca.urls')),
    path('', include('biblioteca.urls')),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)