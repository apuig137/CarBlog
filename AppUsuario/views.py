from django.contrib import messages
from django.shortcuts import render, redirect
from AppUsuario.forms import SignUpForm, AvatarForm
from AppUsuario.models import Avatar
from django.contrib.auth.decorators import login_required
import os

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
        else:
            print("no valido")   
        messages.info(request,"Usuario editado correctamente")
        return redirect("inicio")
    contexto = {
        "form": AvatarForm(),
    }
    return render(request, "editar_avatar.html", contexto)