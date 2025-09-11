# receitas/views.py
from django.shortcuts import render, get_object_or_404
from .models import Receita

def home(request):
        # Obtém uma categoria do parâmetro da URL (ex: /?categoria=drink)
        categoria_slug = request.GET.get('categoria')

        categorias_choices = [choice[0] for choice in Receita.CATEGORIAS]

        if categoria_slug:
        #Se uma categoria for selecionada, filtra as receitas
            receitas = Receita.objects.filter(categoria=categoria_slug)
        # Passa a categoria selecionada para o template, útil para destacar o limk do menu
            categoria_selecionada = categoria_slug
            
        else:
            receitas = Receita.objects.all()
            categoria_selecionada = None
    
        return render(request, 'receitas/home.html', {
            'receitas': receitas,
            'categorias': categorias_choices,
            'categoria_selecionada': categoria_selecionada,})
# Você pode passar 'pesquis' aqui também se quiser unificar tudo

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
