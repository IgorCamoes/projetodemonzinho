from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')
    
def paginaJogos(request):
    return render(request, 'jogos.html')

def lcpagina(request):
    return render(request, 'logincadastro.html')