from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    texto = forms.CharField(widget=forms.TextInput(attrs={'cols': 80, 'rows': 10}))
    class Meta:
        model = Comentario
        fields = ('autor', 'email', 'url', 'texto')
        
