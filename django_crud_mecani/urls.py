from django.contrib import admin
from django.urls import path
from tasks import views # se importan las vistas que se crearon anteriormente

urlpatterns = [
    path('admin/', admin.site.urls), #panel azul
    path('panel/', views.panel_inicio, name='panel'),# nueva pag 
]
