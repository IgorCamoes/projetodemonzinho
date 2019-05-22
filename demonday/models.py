from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField


class Plataformas(models.Model):
    platOptions = [
        ('PS4', 'Playstation 4'),
        ('PS3', 'Playstation 3'),
        ('XONE', 'Xbox One'),
        ('X360', 'Xbox 360'),
        ('PC', 'PC'),
        ('MOBILE', 'Mobile'),
        ('NSwitch', 'Nintendo Switch'),
        ('NDS', 'Nintendo 3DS')
    ]

    plataforma = models.CharField(max_length=6, choices=platOptions, default='Plataforma')
    
    def __str__(self):
        return self.plataforma

class Jogos(models.Model):
    titulo = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='capaJogos/', null=True)
    plataformas = models.ManyToManyField(Plataformas, db_table=None)

    def __str__(self):
        return self.titulo

class UsrIcon(models.Model):
    nome = models.CharField(max_length=5)
    iconOptions = models.ImageField(upload_to='iconesUsr/')

    def __str__(self):
        return self.nome

class DiasDisponiveis(models.Model):
    diasOptions = [
        ('td', 'Todos os dias'),
        ('ss', 'De segunda a sexta'),
        ('fs', 'Finais de semana'),
        ('se', 'Segundas-feiras'),
        ('te', 'Terças-feiras'),
        ('qa', 'Quartas-feiras'),
        ('qi', 'Quintas-feiras'),
        ('sx', 'Sextas-feiras'),
        ('sa', 'Sábados'),
        ('dm', 'Domingos')
    ]

    dispDia = models.CharField(max_length=2, choices=diasOptions)  

    def __str__(self):
        return self.dispDia

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nomeR = models.CharField(max_length=40, blank=True)
    jogos = models.ManyToManyField(Jogos, db_table=None)
    dispDia = models.ManyToManyField(DiasDisponiveis, db_table=None)
    iniHora = models.TimeField(blank=True, default=0)
    fimHora = models.TimeField(blank=True, default=0)
    icon = models.ForeignKey(UsrIcon, on_delete=models.CASCADE, default=None)
    bio = models.TextField(max_length=300)
    discord = models.CharField(max_length=50, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,11}$', message="Numero de celular deve conter apenas números.")
    whatsapp = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    facebook = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.usuario.username

class UsrPosts(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=70)
    jogo = models.ForeignKey(Jogos, null=True, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataformas, on_delete=models.CASCADE)
    horario = models.TimeField(default=0, null=False)
    comentario = models.TextField(max_length=250)

    def __str__(self):
        return self.titulo
    