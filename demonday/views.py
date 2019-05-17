from django.shortcuts import render, redirect
from demonday.models import Jogos, Plataformas, Perfil
from demonday.forms import UsrPerfil, UsrRegistro

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
    if request.method == 'POST' or None:
        # formUser = UsrRegistro(request.POST)
        # formPerfil = UsrPerfil(request.POST)
        if formUser.is_valid() and formPerfil.is_valid:
            formUser.save()
            formPerfil.save()
            pessoa = formUser.cleaned_data.get('usuario')
            messages.success(request, f'Conta criada com sucesso, {pessoa}')
            return redirect('login')

    # contexto={
    #     'form1':formUser,
    #     'form2':formPerfil
    # }

    return render(request, 'logincadastro.html')

