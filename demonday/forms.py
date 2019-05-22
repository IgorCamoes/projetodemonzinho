from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import CheckboxSelectMultiple
from demonday.models import Perfil, UsrPosts, DiasDisponiveis, UsrIcon, Jogos
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe
from demonday.select_time_widget import SelectTimeWidget
from multiselectfield import MultiSelectField


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

class UsrPerfilForm(UserCreationForm):
    icon = FieldComIcone(widget=forms.RadioSelect, queryset=UsrIcon.objects.all(), label='Avatar')
    jogos = FieldComFoto(widget=forms.CheckboxSelectMultiple, queryset=Jogos.objects.all())
    class Meta:
        model = Perfil
        
        fields = ['nomeR', 'jogos', 'icon', 'bio', 'discord', 'whatsapp', 'facebook']
        
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

    def clean(self):
        if not self.discord or self.whatsapp or self.facebook:
            raise ValidationError("Você precisa de pelo menos um meio de contato preenchido!")
        

    def save(self, commit=True):
        usuario = super().save(commit=False)

        usuario.nomeR = self.cleaned_data['nomeR']
        usuario.bio = self.cleaned_data['bio']

        if commit:
            usuario.save()
        return usuario

class UsrPerfilForm2(forms.ModelForm):

    icon = FieldComIcone(widget=forms.RadioSelect, queryset=UsrIcon.objects.all(), label='Avatar')
    jogos = FieldComFoto(widget=forms.CheckboxSelectMultiple, queryset=Jogos.objects.all())

    class Meta:

        dias = DiasDisponiveis.objects.all()
        model = Perfil
        
        fields = ['jogos', 'dispDia', 'iniHora', 'fimHora', 'icon',]
        
        labels = {
            'jogos':'Jogos',
            'dispDia':'Dias disponíveis',
            'iniHora':'Das',
            'fimHora':'Até',
        }

        widgets = {
            'iniHora':SelectTimeWidget(minute_step=5, use_seconds=False),
            'fimHora':SelectTimeWidget(minute_step=5, use_seconds=False),
            'dispDia':forms.Select(attrs={'class':'dispDiaSelect'}, choices=dias)
        }


class UsrPostsForm(forms.ModelForm):
    class Meta:
        model = UsrPosts
        fields = ['titulo', 'jogo', 'plataforma', 'horario', 'comentario']
