from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), #criando url apontada para a área adminstrativa do DJANGO
    path('', include('my_dashboard.urls')) #criando a url para o projeto
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #url para servir ao arquivos estáticos (js, css...)




