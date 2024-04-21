# Criar um arquivo igual o 'urls.py' do projeto
from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_curriculo', views.cadastrar_curriculo, name='cadastrar_curriculo'),
    path('sucesso', views.sucesso, name='sucesso'),
    path('listar_curriculos', views.listar_curriculos, name='listar_curriculos'),
    path('editar_curriculos', views.editar_curriculos, name='editar_curriculos'),
]

