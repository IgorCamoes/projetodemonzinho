from django.contrib import admin
from demonday.models import Jogos, Plataformas, UsrIcon, Usuario, DiasDisponiveis

# Register your models here.

admin.site.register(Jogos)
admin.site.register(Plataformas)
admin.site.register(UsrIcon)
admin.site.register(Usuario)
admin.site.register(DiasDisponiveis)