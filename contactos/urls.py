from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('guardar/', views.guardar_contacto, name='guardar_contacto'),
    path('editar/<int:id>/', views.editar_contacto, name='editar_contacto'),
    path('eliminar/<int:id>/', views.eliminar_contacto, name='eliminar_contacto'),
]