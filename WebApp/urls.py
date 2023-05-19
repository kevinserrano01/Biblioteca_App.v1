from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # user: admin - password: admin123
    path('biblioteca/', include('biblioteca.urls')),
]