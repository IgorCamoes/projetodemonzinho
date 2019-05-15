from django.shortcuts import render
from demonday.models import Jogos, Plataformas

# Create your views here.

def index(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')
    
def feed(request):
    return render(request, 'feed.html')
    
def paginaJogos(request):
    jogo = Jogos.objects.all()
    plataforma = Plataformas.objects.all()

    contexto = {
        'jogos' : jogo,
        'plataforma' : plataforma
    }
    return render(request, 'jogos.html', contexto)

def lcpagina(request):
    return render(request, 'logincadastro.html')
