from django.urls import path
from .views import listar_trabajadores, crear_trabajador,editar_trabajador,eliminar_trabajador




urlpatterns = [
    path('rh/listarTrabajador/', listar_trabajadores, name='list_trab'),
    path('crear_trabajador/',crear_trabajador, name='crear_trabajador'),
    path('editar_trabajador/<int:pk>/', editar_trabajador, name='editar_trabajador'),
    path('eliminar_trabajador/<int:pk>/',eliminar_trabajador, name='eliminar_trabajador'),
    
]

