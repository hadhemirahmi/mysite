from django import forms 
from .models import Jeu 
class JeuForm(forms.ModelForm):
    class Meta:
        model = Jeu
        fields = '__all__'
        