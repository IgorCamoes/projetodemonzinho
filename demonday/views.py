from django.shortcuts import render, redirect
from demonday.models import Jogos, Plataformas, Perfil
from demonday.forms import UsrPerfil, UsrRegistro
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    jogo = Jogos.objects.all()
    return render(request, 'index.html', {'jogos':jogo})

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
    formUser = UsrRegistro(request.POST or None)
    formPerfil = UsrPerfil(request.POST or None)

    if request.method == 'POST':
        formUser = UsrRegistro(request.POST)
        formPerfil = UsrPerfil(request.POST)   
        
        if formUser.is_valid() and formPerfil.is_valid():
            usuario = formUser.save()
            perfil = formPerfil.save(commit=False)
            perfil.usuario = usuario

            perfil.save()



            username = formUser.cleaned_data.get('username')
            senha = formUser.cleaned_data.get('password1')
            usuario = authenticate(username=username, password=senha)
            return redirect('home')
        
        else:
            formUser = UsrRegistro()
            formPerfil = UsrPerfil()

    contexto={
        'form1':formUser,
        'form2':formPerfil
    }

    return render(request, 'logincadastro.html', contexto)

