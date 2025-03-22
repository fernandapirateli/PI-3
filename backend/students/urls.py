from django.urls import path
from . import views

urlpatterns = [
    path('registrar_aluno', views.registrar_aluno, name='registrar_aluno'),
]
