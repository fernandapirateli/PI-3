from django.urls import path
from . import views

urlpatterns = [
    path('listar_alimentos', views.listar_alimentos, name='listar_alimentos'),
    path('detalhes_alimento', views.detalhes_alimento, name='detalhes_alimento'),
    path('somar_alimentos', views.somar_alimentos, name='somar_alimentos'),
]
