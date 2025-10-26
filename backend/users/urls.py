from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar', views.registrar, name='registrar'),
    path('perfil', views.perfil, name='perfil'),
    path('logar', views.logar, name='logar'),
    path('deslogar', views.deslogar, name='deslogar'),
    path('relatorio_alunos', views.relatorio_alunos, name='relatorio_alunos')
]
