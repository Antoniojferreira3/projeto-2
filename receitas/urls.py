# receitas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

# Adicionando as rotas para novas páginas

    path('sobre_nos/', views.sobre_nos, name='sobre_nos'),
    path('contato/', views.contato, name='contato'),
    path('sucesso/', views.sucesso, name='sucesso'),

    # As rotas a seguir já estavam corretas e devem ser mantidas

    path('receita/<int:id>/', views.receita_detail, name='receita_detail'),
    path('pesquisar/', views.pesquisar_receitas, name='pesquisar_receitas'),
]