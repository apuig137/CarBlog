from django import forms

class AutoFormulario(forms.Form):
    titulo=forms.CharField(max_length=30)
    subtitulo=forms.CharField(max_length=40)
    cuerpo=forms.CharField(max_length=200)
    autor=forms.CharField(max_length=20)
    imagen=forms.ImageField(required=False)

class MotoFormulario(forms.Form):
    titulo=forms.CharField(max_length=30)
    subtitulo=forms.CharField(max_length=40)
    cuerpo=forms.CharField(max_length=200)
    autor=forms.CharField(max_length=20)
    imagen=forms.ImageField(required=False)

class CamionetaFormulario(forms.Form):
    titulo=forms.CharField(max_length=30)
    subtitulo=forms.CharField(max_length=40)
    cuerpo=forms.CharField(max_length=200)
    autor=forms.CharField(max_length=20)
    imagen=forms.ImageField(required=False)

class VehiculoBusqueda(forms.Form):
    titulo=forms.CharField(max_length=30)