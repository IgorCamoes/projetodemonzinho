from django import forms
from django.contrib.auth.models import User
from demonday.models import Perfil
from django.contrib.auth.forms import UserCreationForm

class UsrRegistro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UsrPerfil(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['jogos', 'dispDia', 'icon', 'bio']