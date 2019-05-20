from django import forms
from django.contrib.auth.models import User
from demonday.models import Perfil, UsrPosts, DiasDisponiveis, UsrIcon
from django.contrib.auth.forms import UserCreationForm
from demonday.select_time_widget import SelectTimeWidget

class UsrRegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UsrPerfilForm(forms.ModelForm):

    dispDia=forms.ChoiceField(widget=forms.Select(attrs={'class':'dispDiaSelect'}), choices=DiasDisponiveis.diasOptions)
    icon=forms.ModelChoiceField(UsrIcon.objects.all(), widget=forms.RadioSelect)

    class Meta:
        model = Perfil
        
        fields = ['nomeR', 'jogos', 'dispDia', 'iniHora', 'fimHora', 'icon', 'bio', 'discord', 'whatsapp', 'facebook']
        
        labels = {
            'nomeR':'Nome Real (opcional)',
            'jogos':'Jogos',
            'dispDia':'Dias disponíveis',
            'iniHora':'Das',
            'fimHora':'Até',
            'icon':'Avatar',
            'bio':'Sobre você',
            'discord':'Discord',
            'whatsapp':'WhatsApp',
            'facebook':'Facebook'
        }

        widgets = {
            'iniHora':SelectTimeWidget(minute_step=5, use_seconds=False),
            'fimHora':SelectTimeWidget(minute_step=5, use_seconds=False),
            'bio':forms.Textarea(attrs={'placeholder':'Escreva aqui um pouco sobre como você é quando está jogando online... Um player mais casual? Ou talvez alguém atras do competitivo?'}),
        }

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
