from django.db import models

# Create your models here.

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
    capa = models.ImageField(upload_to='', null=True)
    plataforma = models.ManyToManyField(Plataformas)

    def __str__(self):
        return self.titulo
