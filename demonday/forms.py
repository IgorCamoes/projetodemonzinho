from django import forms
from django.contrib.auth.models import User
from demonday.models import Perfil, UsrPosts, DiasDisponiveis, UsrIcon, Jogos
from django.contrib.auth.forms import UserCreationForm
from demonday.select_time_widget import SelectTimeWidget
from multiselectfield import MultiSelectField


class UsrRegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UsrPerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        
        fields = ['nomeR', 'bio', 'discord', 'whatsapp', 'facebook']
        
        labels = {
            'nomeR':'Nome Real (opcional)',
            'bio':'Sobre você',
            'discord':'Discord',
            'whatsapp':'WhatsApp',
            'facebook':'Facebook'
        }

        widgets = {
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

class UsrPerfilForm2(forms.ModelForm):
    class Meta:

        jogos = Jogos.objects.all().values('titulo','plataformas')
        dias = DiasDisponiveis.objects.all()
        model = Perfil
        
        fields = ['jogos', 'dispDia', 'iniHora', 'fimHora', 'icon',]
        
        labels = {
            'jogos':'Jogos',
            'dispDia':'Dias disponíveis',
            'iniHora':'Das',
            'fimHora':'Até',
            'icon':'Avatar',
        }
        # dispDia = (widget=forms.Select(attrs={'class':'dispDiaSelect'}), choices=DiasDisponiveis)
        jogos = MultiSelectField(choices=jogos),


        widgets = {
            # 'jogos':MultiSelectField(choices=jogos),
            'iniHora':SelectTimeWidget(minute_step=5, use_seconds=False),
            'fimHora':SelectTimeWidget(minute_step=5, use_seconds=False),
            'dispDia':forms.Select(attrs={'class':'dispDiaSelect'}, choices=dias),
            'icon':forms.RadioSelect(attrs={'class':'iconSelect'})
        }


class UsrPostsForm(forms.ModelForm):
    class Meta:
        model = UsrPosts
        fields = ['titulo', 'jogo', 'plataforma', 'horario', 'comentario']
