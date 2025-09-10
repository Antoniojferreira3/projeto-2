# receitas/views.py
from django.shortcuts import render, get_object_or_404
from .models import Receita

def home(request):
    # Pega todas as receitas do banco
 
        receitas = Receita.objects.all()

    # Envia o dicionário {'receitas': receitas} para o template
        return render(request, 'receitas/home.html', {'receitas': receitas})

def receita_detail(request, id):
    # Busca a receita pelo ID ou retorna um erro 404 se não existir
        receita=get_object_or_404(Receita, pk=id)
        return render(request, 'receitas/receita_detail.html', {'receita': receita})

def pesquisar_receitas(request):
        query=request.GET.get('q','') # Pega o termo digitado na busca
        resultados=[]
        if query:
    #Busca receitas cujo título contenha o termo (case-insensitive)
            resultados=Receita.objects.filter(title__icontains=query)
            return render(request, 'receitas/pesquisa.html', {'resultados': resultados, 'query': query})
