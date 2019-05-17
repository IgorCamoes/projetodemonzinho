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
        fields = ['nomeR', 'jogos', 'dispDia', 'icon', 'bio']

    def save(self, commit=True):
        usuario = super().save(commit=False)

        usuario.nomeR = self.cleaned_data['nomeR']
        usuario.bio = self.cleaned_data['bio']

        if commit:
            usuario.save()
        return usuario