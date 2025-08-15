from django.shortcuts import render 
 
# receitas/views.py 
def home(request): 
    return render(request, 'receitas/home.html') 