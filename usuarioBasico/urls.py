# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('inicio/', views.iniciosesion, name = "iniciosesion"),
    path('logout/', views.logout_view, name='logout'),
]