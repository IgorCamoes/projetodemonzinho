from django.contrib import admin
from demonday.models import Jogos, Plataformas, UsrIcon, DiasDisponiveis, Perfil
from django.db import models

# Register your models here.

admin.site.register(Jogos)
admin.site.register(Plataformas)
admin.site.register(UsrIcon)
admin.site.register(DiasDisponiveis)
admin.site.register(Perfil)

