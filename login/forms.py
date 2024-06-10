from django import forms
from .models import *

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre_user', 'foto']
        widgets = {
            'nombre_user': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'})
        }