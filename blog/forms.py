from django.forms import ModelForm
from .models import Post
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class blogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "title", "content", "status", "image"

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

