from django.urls import path
from . import views

urlpatterns = [
    path('registrar_aluno', views.registrar_aluno, name='registrar_aluno'),
    path('listar_alunos', views.listar_alunos, name='listar_alunos'),
    path('perfil_aluno', views.perfil_aluno, name='perfil_aluno'),
]
