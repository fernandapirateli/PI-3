from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar', views.registrar, name='registrar'),
    path('logar', views.logar, name='logar'),
    path('logout', views.logout, name='logout'),
]
