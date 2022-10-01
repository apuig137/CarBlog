from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from AppUsuario.models import Avatar

class SignUpForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=("username","email")

class AvatarForm(forms.Form):
    imagen = forms.ImageField()

class MensajeForm(forms.Form):
    mensaje=forms.CharField(max_length=50)