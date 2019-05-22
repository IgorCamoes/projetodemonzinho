from django import views
from django.shortcuts import render, redirect
from demonday.models import Jogos, Plataformas, Perfil, UsrIcon, UsrPosts
from demonday.forms import UsrPerfilForm, UsrRegistroForm, UsrPostsForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    jogo = Jogos.objects.all()
    posts = UsrPosts.objects.all()

    contexto={
        'jogos':jogo,
        'posts':posts
    }
    return render(request, 'index.html', contexto)

def perfil(request):
    perfil = Perfil.objects.all()
    posts = UsrPosts.objects.all()
    
    contexto={
        'perfil':perfil,
        'post':posts
    }

    return render(request, 'perfil.html', contexto)

def pega_o_user(request, username):
    user = User.objects.get(username=username)
    return render(request, 'user.html', {"usuario":user})
    
def feed(request):
    perfil = Perfil.objects.all()
    posts = UsrPosts.objects.all()
    feedFilter = UsrPosts.objects.prefetch_related('jogos').all()
    form_Post = UsrPostsForm(request.POST or None)
    

    if request.method == 'POST':
        form_Post = UsrPostsForm(request.POST)

        if form_Post.is_valid():

            novoform_Post = form_Post.save(commit=False)
            novoform_Post.usuario = request.user
            novoform_Post.save()
            titulo = form_Post.cleaned_data.get('titulo')
            comentario = form_Post.cleaned_data.get('comentario')
            horario = form_Post.cleaned_data.get('horario')
            
        
        else:
            form_Post = UsrPostsForm()

            
            
    contexto={
        'form':form_Post,
        'perfil':perfil,
        'posts':posts,
        'match':feedFilter
        }
        
    return render(request, 'feed.html', contexto)
    
def paginaJogos(request):
    jogo = Jogos.objects.all()
    posts = UsrPosts.objects.all()
    plataforma = Plataformas.objects.all()

    contexto = {
        'jogos' : jogo,
        'plataforma' : plataforma,
        'posts':posts
    }
    return render(request, 'jogos.html', contexto)

def cadastro(request):
    formUser = UsrRegistroForm(request.POST or None)
    formPerfil = UsrPerfilForm(request.POST or None)
    msg = ''

    if request.method == 'POST':
        formUser = UsrRegistroForm(request.POST)
        formPerfil = UsrPerfilForm(request.POST)
        
        if formUser.is_valid() and formPerfil.is_valid():
            usuario = formUser.save()
            perfil = formPerfil.save(commit=False)
            perfil.usuario = usuario
            perfil.save()
            msg = 'Conta criada com sucesso'
            username = perfil.cleaned_data.get('username')
            senha = perfil.cleaned_data.get('password1')
            discord =  perfil.cleaned_data.get('discord')
            whatsapp =  perfil.cleaned_data.get('whatsapp')
            facebook =  perfil.cleaned_data.get('facebook')
            usuario = authenticate(username=username, password=senha)
            return redirect('home')
        
        else:
            formUser = UsrRegistroForm()
            formPerfil = UsrPerfilForm()

    contexto={
        'form1':formUser,
        'form2':formPerfil,
        'msg':msg
    }

    return render(request, 'cadastro.html', contexto)

def login(request):
    
    return render(request, 'login.html')