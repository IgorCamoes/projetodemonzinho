from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Plataformas(models.Model):
    platOptions = [
        ('p4', 'Playstation 4'),
        ('p3', 'Playstation 3'),
        ('xo', 'Xbox One'),
        ('x3', 'Xbox 360'),
        ('pc', 'PC'),
        ('mo', 'Mobile'),
        ('ns', 'Nintendo Switch'),
        ('nd', 'Nintendo 3DS')
    ]

    plataforma = models.CharField(max_length=2, choices=platOptions, default='Plataforma')
    
    def __str__(self):
        return self.plataforma

class Jogos(models.Model):
    titulo = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='capaJogos/', null=True)
    plataforma = models.ManyToManyField(Plataformas)

    def __str__(self):
        return self.titulo

class UsrIcon(models.Model):
    nome = models.CharField(max_length=5)
    iconOptions = models.ImageField(upload_to='iconesUsr/')

    def __str__(self):
        return self.nome

class DiasDisponiveis(models.Model):
    diasOptions = [
        ('se', 'Segunda-feiras'),
        ('te', 'Terça-feiras'),
        ('qa', 'Quarta-feiras'),
        ('qi', 'Quinta-feiras'),
        ('sx', 'Sexta-feiras'),
        ('sa', 'Sábados'),
        ('dm', 'Domingos')
    ]

    dispDia = models.CharField(max_length=2, choices=diasOptions)
    
    def __str__(self):
        return self.dispDia

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nomeR = models.CharField(max_length=40, blank=True)
    jogos = models.ManyToManyField(Jogos)
    dispDia = models.ManyToManyField(DiasDisponiveis)
    icon = models.ForeignKey(UsrIcon, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300)

    def __str__(self):
        return self.usuario.username