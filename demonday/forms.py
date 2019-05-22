from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import CheckboxSelectMultiple
from demonday.models import Perfil, UsrPosts, DiasDisponiveis, UsrIcon, Jogos
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe
from demonday.select_time_widget import SelectTimeWidget

class FieldComIcone(forms.ModelChoiceField):

    def label_from_instance(self, obj):
        return mark_safe("<img class='iconeForm' src='%s'/>" % obj.iconOptions.url)

class FieldComFoto(forms.ModelChoiceField):

    def label_from_instance(self, obj):
        return mark_safe("<img class='capaForm' src='%s'/>" % obj.capa.url)

class UsrRegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UsrPerfilForm(forms.ModelForm):
    icon = FieldComIcone(widget=forms.RadioSelect, queryset=UsrIcon.objects.all())
    jogos = FieldComFoto(widget=forms.CheckboxSelectMultiple, queryset=Jogos.objects.all())
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
            'dispDia':forms.Select(attrs={'class':'dispDiaSelect'}, choices=DiasDisponiveis.diasOptions),
            'icon':forms.RadioSelect(attrs={'class':'iconSelect'}),
        }

        

    def save(self, commit=True):
        usuario = super().save(commit=False)

        usuario.nomeR = self.cleaned_data['nomeR']
        usuario.bio = self.cleaned_data['bio']

        if commit:
            usuario.save()
        return usuario

class UsrPostsForm(forms.ModelForm):
    class Meta:
        model = UsrPosts
        fields = ['titulo', 'jogo', 'plataforma', 'horario', 'comentario']
