from django import views
from django.shortcuts import render, redirect
from demonday.models import Jogos, Plataformas, Perfil, UsrIcon, UsrPosts
from demonday.forms import UsrPerfilForm, UsrRegistroForm, UsrPostsForm, UsrPerfilForm2
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
    eu = UsrPosts.objects.all().filter(usuario__username='Juliafc')


    contexto={
        'perfil':perfil,
        'post':posts,
        'eu':eu
    }

    return render(request, 'perfil.html', contexto)

def pega_o_user(request, username):
    user = User.objects.get(username=username)
    post = UsrPosts.objects.all().filter(usuario__username='%s' % user)

    contexto={
        "usuario":user,
        'post':post
    }
    return render(request, 'user.html', contexto)
    
def feed(request):
    perfil = Perfil.objects.all()
    posts = UsrPosts.objects.all()
    form_Post = UsrPostsForm(request.POST or None)
    feedFilter = UsrPosts.objects.all().filter(usuario__username='Skorthix')
    

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
    ow = UsrPosts.objects.all().filter(jogo__titulo='Overwatch')

    contexto = {
        'jogos' : jogo,
        'plataforma' : plataforma,
        'posts':posts,
        'ow':ow
    }
    return render(request, 'jogos.html', contexto)

def cadastro(request):
    formUser = UsrRegistroForm(request.POST or None)
    formPerfil = UsrPerfilForm(request.POST or None)
    formPerfil2 = UsrPerfilForm2(request.POST or None)
    msg= ''


    if request.method == 'POST':
        formUser = UsrRegistroForm(request.POST)
        formPerfil = UsrPerfilForm(request.POST)  
        formPerfil2 = UsrPerfilForm2(request.POST)  
        
        if formUser.is_valid() and formPerfil.is_valid() and formPerfil2.is_valid():
            usuario = formUser.save()
            perfil = formPerfil.save(commit=False)
            perfil2 = formPerfil2.save(commit=False)
            perfil.usuario = usuario
            perfil2.usuario = usuario
            perfil.save()
            perfil2.save()
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
            formPerfil2 = UsrPerfilForm2()


    contexto={
        'form1':formUser,
        'form2':formPerfil,
        'form3':formPerfil2,
        'msg':msg
    }

    return render(request, 'cadastro.html', contexto)

def login(request):
    
    return render(request, 'login.html')