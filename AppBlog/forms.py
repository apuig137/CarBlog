from django import forms
from AppBlog.models import AutoImagen, CamionetaImagen, MotoImagen

class AutoFormulario(forms.Form):
    titulo=forms.CharField(max_length=30)
    subtitulo=forms.CharField(max_length=40)
    cuerpo=forms.CharField(max_length=200)
    autor=forms.CharField(max_length=20)

class AutoImagenFormulario(forms.ModelForm):
    class Meta:
        model=AutoImagen
        fields="__all__"

class MotoFormulario(forms.Form):
    titulo=forms.CharField(max_length=30)
    subtitulo=forms.CharField(max_length=40)
    cuerpo=forms.CharField(max_length=200)
    autor=forms.CharField(max_length=20)

class MotoImagenFormulario(forms.ModelForm):
    class Meta:
        model=MotoImagen
        fields="__all__"

class CamionetaFormulario(forms.Form):
    titulo=forms.CharField(max_length=30)
    subtitulo=forms.CharField(max_length=40)
    cuerpo=forms.CharField(max_length=200)
    autor=forms.CharField(max_length=20)

class CamionetaImagenFormulario(forms.ModelForm):
    class Meta:
        model=CamionetaImagen
        fields="__all__"

class VehiculoBusqueda(forms.Form):
    titulo=forms.CharField(max_length=30)