from django.urls import path
from . import views

urlpatterns = [
    # 1. Rotas Principais do Projeto
    path('', views.iniciar_jogo, name='home'),
    # path('estilo/', views.estilo_page, name='estilo_page'), # Sem uso 

    # 2. Rotas do Formulário e Persistência
    path('contato/', views.contato, name='contato'),
    path('salvar-contato/', views.salvar_contato, name='salvar_contato'),
    path('contatos-salvos/', views.listar_contatos, name='listar_contatos'),

    # 3. Rotas do Jogo da Forca
    path('forca/', views.jogar_forca, name='jogar_forca'),
    path('forca/iniciar/', views.iniciar_jogo, name='iniciar_jogo'),
]