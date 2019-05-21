from django.shortcuts import render, redirect
from demonday.models import Jogos, Plataformas, Perfil, UsrIcon, UsrPosts
from demonday.forms import UsrPerfilForm, UsrRegistroForm, UsrPostsForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    jogo = Jogos.objects.all()
    return render(request, 'index.html', {'jogos':jogo})

def perfil(request):
    return render(request, 'perfil.html')
    
def feed(request):
    formPost = UsrPostsForm(request.POST or None)
    perfil = Perfil.objects.all()

    if request.method == 'POST':
        formPost = formPost(request.POST)

        if formPost.is_valid():
            post = formPost.save()
            titulo = formPost.cleaned_data.get('titulo')
            comentario = formPost.cleaned_data.get('comentario')
            
    contexto={
        'form':formPost,
        'perfil':perfil,
        'nomeR':Perfil.nomeR
        }
        
    print(perfil)
    return render(request, 'feed.html', contexto)
    
def paginaJogos(request):
    jogo = Jogos.objects.all()
    plataforma = Plataformas.objects.all()

    contexto = {
        'jogos' : jogo,
        'plataforma' : plataforma
    }
    return render(request, 'jogos.html', contexto)

def cadastro(request):
    formUser = UsrRegistroForm(request.POST or None)
    formPerfil = UsrPerfilForm(request.POST or None)

    if request.method == 'POST':
        formUser = UsrRegistroForm(request.POST)
        formPerfil = UsrPerfilForm(request.POST)  
        form.fields["icon"].queryset = UsrIcon.objects.all() 
        
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
            formUser = UsrRegistroForm()
            formPerfil = UsrPerfilForm()

    contexto={
        'form1':formUser,
        'form2':formPerfil
    }

    return render(request, 'cadastro.html', contexto)

def login(request):
    
    return render(request, 'login.html')