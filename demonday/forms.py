from django import forms
from django.contrib.auth.models import User
from demonday.models import Perfil, UsrPosts
from django.contrib.auth.forms import UserCreationForm

class UsrRegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UsrPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nomeR', 'jogos', 'dispDia', 'icon', 'bio', 'discord', 'whatsapp', 'facebook']

    def save(self, commit=True):
        usuario = super().save(commit=False)

        usuario.nomeR = self.cleaned_data['nomeR']
        usuario.bio = self.cleaned_data['bio']
        usuario.facebook = self.cleaned_data['facebook']
        usuario.whatsapp = self.cleaned_data['whatsapp']

        if commit:
            usuario.save()
        return usuario

class UsrPostsForm(forms.ModelForm):
    class Meta:
        model: UsrPosts
        fields = ['titulo', 'jogo', 'plataformas', 'horario', 'comentario']