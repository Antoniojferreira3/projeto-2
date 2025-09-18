# receitas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import Receita
from .forms import ContatoForm

def sobre_nos(request):
    return render(request, 'receitas/sobre_nos.html')

def contato (request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

# função que salva e-mail
            send_mail( 
                f'Mensagem de {nome}',
                f'Mensagem de {nome} ({email}):\n\n{mensagem}',
                email,
                ['seu_email_para_receber@exemplo.com'],
                fail_silently=False,
            )
# Depois de enviar o e-mail, você pode redirecionar ou mostrar uma mensagem de sucesso
            return redirect(reverse('sucesso'))
    else:
        form = ContatoForm()
    return render(request, 'receitas/contato.html', {'form': form})
def sucesso(request):
    return render(request, 'receitas/sucesso.html')

# Obtém uma categoria do parâmetro da URL (ex: /?categoria=drink)
def home(request):        
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
