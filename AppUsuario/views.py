from django.contrib import messages
from django.shortcuts import render, redirect
from AppUsuario.forms import SignUpForm, AvatarForm
from AppUsuario.models import Avatar
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os

from AppUsuario.forms import MensajeForm

def signup(request):
    if request.method == "POST":
        mi_formulario = SignUpForm(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
            messages.info(request,"Usuario registrado correctamente, inicie sesion para disfrutar de nuestra pagina!")
        else:
            messages.info(request,"Contraseña o usuario incorrecto")
        return redirect("inicio")
    contexto = {
        "form" : SignUpForm(),
    }
    return render(request,"registration/signup.html",contexto)

@login_required
def editar_perfil(request):
    usuario=request.user
    if request.method == "POST":
        mi_formulario = SignUpForm(request.POST)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            usuario.username=data.get("username")
            usuario.email=data.get("email")
            usuario.save()
            messages.info(request,"Usuario editado correctamente")
        else:
            messages.info(request,"No se pudo editar el usuario")
        return redirect("inicio")
    contexto = {
        "form" : SignUpForm(
            initial={
                "username":usuario.username,
                "email":usuario.email,
            }
        ),
    }
    return render(request,"editar_perfil.html",contexto)

@login_required
def editar_avatar(request):
    if request.method == "POST":
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            try:
                post = Avatar.objects.get(user=request.user)
                try:
                    os.remove(post.imagen.path)
                    print('Old post image deleted...! path = '+str(post.imagen.path))
                except Exception as e:
                    print('No image for delete '+str(e))
                    post.imagen = request.FILES['imagen']
                post.save()
            except Exception as e:
                    print(e) 
            messages.info(request,"Usuario editado correctamente")
        else:
            messages.info(request,"No se pudo editar")   
        return redirect("inicio")
    contexto = {
        "form": AvatarForm(),
    }
    return render(request, "editar_avatar.html", contexto)
    

@login_required
def agregar_avatar(request):
    if request.method == "POST":
        mi_formulario = AvatarForm(request.POST,request.FILES)
        if mi_formulario.is_valid():
            u=User.objects.get(username=request.user)
            avatar=Avatar(user=u,imagen=mi_formulario.cleaned_data["imagen"])
            avatar.save()
            return render(request,"index.html")
    else:
        mi_formulario=AvatarForm
    return render(request,"editar_avatar.html",{"form":mi_formulario})


"""def editar_avatar(request):
    if request.method == "POST":
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            avatar = Avatar.objects.filter(user=data.get("usuario"))
            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()
            else:
                avatar = Avatar(user=data.get("user"), imagen=data.get("imagen"))
                avatar.save()
        return redirect("inicio")
    contexto = {
        "form": AvatarForm()
    }
    return render(request, "editar_avatar.html", contexto)
"""
