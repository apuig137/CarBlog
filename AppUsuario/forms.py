from AppUsuario.models import Avatar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email=forms.EmailField()
    avatar=forms.ImageField()
    class Meta:
        model=User
        fields=("username","email")

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen")