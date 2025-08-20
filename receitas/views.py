from django.shortcuts import render 
from django.http import Http404
 
# receitas/views.py 
def home(request): 

    return render(request, 'receitas/home.html') 

def receita_detail(request, id):

    context = {
        'receita_id': id,
        'receita_title': f'Receita Detalhada {id}', # Exemplo de título
        'receita_description': f'Esta é a descrição detalhada da receita com ID {id}.'
    }
