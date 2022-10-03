from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppBlog.models import *
from AppUsuario.models import *
from AppBlog.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

def inicio(request):
    return render(request,"index.html")

def about(request):
    return render(request,"portafolio.html")

def no_disponible(request):
    return render(request,"no_disponible.html")

@login_required
def auto(request):
    autos=Auto.objects.all()
    contexto={"autos":autos}
    return render(request,"auto.html",contexto)

@permission_required('AppBlog.eliminar_auto/<str:titulo>', login_url='/accounts/login/')
def eliminar_auto(request, titulo):
    auto_eliminar=Auto.objects.get(titulo=titulo)
    auto_eliminar.delete()
    messages.info(request,f"Articulo de {auto_eliminar} eliminado")
    return redirect("auto")

@permission_required('AppBlog.eliminar_auto/<str:titulo>', login_url='/accounts/login/')
def editar_auto(request, titulo):
    auto_editar=Auto.objects.get(titulo=titulo)

    if request.method == "POST":
        mi_formulario = AutoFormulario(request.POST,request.FILES)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            auto_editar.titulo = data.get("titulo")
            auto_editar.subtitulo = data.get("subtitulo")
            auto_editar.cuerpo = data.get("cuerpo")
            auto_editar.autor = data.get("autor")
            auto_editar.imagen = data.get("imagen")
            auto_editar.save()
            return redirect("auto")

    contexto={
        "form":AutoFormulario(
            initial={
                "titulo":auto_editar.titulo,
                "subtitulo":auto_editar.subtitulo,
                "cuerpo":auto_editar.cuerpo,
                "autor":auto_editar.autor,
                "imagen":auto_editar.imagen,
            }
        )
    }
    return render(request,"agregar_auto.html",contexto)

@login_required
def agregar_auto(request):
    if request.method == "POST":
        mi_formulario = AutoFormulario(request.POST,request.FILES)
        print(mi_formulario)
        if mi_formulario.is_valid():
            titulo = mi_formulario.cleaned_data.get("titulo")
            subtitulo = mi_formulario.cleaned_data.get("subtitulo")
            cuerpo = mi_formulario.cleaned_data.get("cuerpo")
            autor = mi_formulario.cleaned_data.get("autor")
            imagen = mi_formulario.cleaned_data.get("imagen")
            obj = Auto.objects.create(titulo=titulo,subtitulo=subtitulo,cuerpo=cuerpo,autor=autor,imagen=imagen)
            obj.save()
            return redirect("auto")
    autos=Auto.objects.all()
    contexto = {
        "form" : AutoFormulario(),
        "autos" : autos,
    }
    return render(request,"agregar_auto.html",contexto)

@login_required
def auto_busqueda(request):
    contexto={
        "form":VehiculoBusqueda(),
    }
    return render(request,"auto_busqueda.html",contexto)

@login_required
def mostrar_auto(request):
    titulo=request.GET.get('titulo')
    autos=Auto.objects.filter(titulo__icontains=titulo)
    contexto={
        "autos":autos,
    }
    return render(request,"mostrar_auto.html",contexto)

@login_required
def ver_auto(request,titulo):
    autos=Auto.objects.filter(titulo__icontains=titulo)
    contexto={
        "autos":autos,
    }
    return render(request,"ver_auto.html",contexto)

@login_required
def moto(request):
    motos=Moto.objects.all()
    contexto={"motos":motos}
    return render(request,"moto.html",contexto)

@permission_required('AppBlog.eliminar_auto/<str:titulo>', login_url='/accounts/login/')
def eliminar_moto(request, titulo):
    moto_eliminar=Moto.objects.get(titulo=titulo)
    moto_eliminar.delete()
    messages.info(request,f"Articulo de {moto_eliminar} eliminado")
    return redirect("moto")

@permission_required('AppBlog.eliminar_auto/<str:titulo>', login_url='/accounts/login/')
def editar_moto(request, titulo):
    moto_editar=Moto.objects.get(titulo=titulo)

    if request.method == "POST":
        mi_formulario = MotoFormulario(request.POST,request.FILES)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            moto_editar.titulo = data.get("titulo")
            moto_editar.subtitulo = data.get("subtitulo")
            moto_editar.cuerpo = data.get("cuerpo")
            moto_editar.autor = data.get("autor")
            moto_editar.imagen = data.get("imagen")
            moto_editar.save()
            return redirect("moto")

    contexto={
        "form":MotoFormulario(
            initial={
                "titulo":moto_editar.titulo,
                "subtitulo":moto_editar.subtitulo,
                "cuerpo":moto_editar.cuerpo,
                "autor":moto_editar.autor,
                "imagen":moto_editar.imagen,
            }
        )
    }
    return render(request,"agregar_moto.html",contexto)

@login_required
def agregar_moto(request):
    if request.method == "POST":
        mi_formulario = MotoFormulario(request.POST,request.FILES)
        print(mi_formulario)
        if mi_formulario.is_valid():
            titulo = mi_formulario.cleaned_data.get("titulo")
            subtitulo = mi_formulario.cleaned_data.get("subtitulo")
            cuerpo = mi_formulario.cleaned_data.get("cuerpo")
            autor = mi_formulario.cleaned_data.get("autor")
            imagen = mi_formulario.cleaned_data.get("imagen")
            obj = Moto.objects.create(titulo=titulo,subtitulo=subtitulo,cuerpo=cuerpo,autor=autor,imagen=imagen)
            obj.save()
            return redirect("moto")
    motos=Moto.objects.all()
    contexto = {
        "form" : MotoFormulario(),
        "motos" : motos,
    }
    return render(request,"agregar_moto.html",contexto)

@login_required
def moto_busqueda(request):
    contexto={
        "form":VehiculoBusqueda(),
    }
    return render(request,"moto_busqueda.html",contexto)

@login_required  
def mostrar_moto(request):
    titulo=request.GET.get('titulo')
    motos=Moto.objects.filter(titulo__icontains=titulo)
    contexto={
        "motos":motos,
    }
    return render(request,"mostrar_moto.html",contexto)

@login_required
def ver_moto(request,titulo):
    motos=Moto.objects.filter(titulo__icontains=titulo)
    contexto={
        "motos":motos,
    }
    return render(request,"ver_moto.html",contexto)

@login_required
def camioneta(request):
    camionetas=Camioneta.objects.all()
    contexto={"camionetas":camionetas}
    return render(request,"camioneta.html",contexto)

@permission_required('AppBlog.eliminar_auto/<str:titulo>', login_url='/accounts/login/')
def eliminar_camioneta(request, titulo):
    camioneta_eliminar=Camioneta.objects.get(titulo=titulo)
    camioneta_eliminar.delete()
    messages.info(request,f"Articulo de {camioneta_eliminar} eliminado")
    return redirect("camioneta")

@permission_required('AppBlog.eliminar_auto/<str:titulo>', login_url='/accounts/login/')
def editar_camioneta(request, titulo):
    camioneta_editar=Camioneta.objects.get(titulo=titulo)

    if request.method == "POST":
        mi_formulario = CamionetaFormulario(request.POST,request.FILES)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            camioneta_editar.titulo = data.get("titulo")
            camioneta_editar.subtitulo = data.get("subtitulo")
            camioneta_editar.cuerpo = data.get("cuerpo")
            camioneta_editar.autor = data.get("autor")
            camioneta_editar.imagen = data.get("imagen")
            camioneta_editar.save()
            return redirect("camioneta")

    contexto={
        "form":CamionetaFormulario(
            initial={
                "titulo":camioneta_editar.titulo,
                "subtitulo":camioneta_editar.subtitulo,
                "cuerpo":camioneta_editar.cuerpo,
                "autor":camioneta_editar.autor,
                "imagen":camioneta_editar.imagen,
            }
        )
    }
    return render(request,"agregar_camioneta.html",contexto)

@login_required
def agregar_camioneta(request):
    if request.method == "POST":
        mi_formulario = CamionetaFormulario(request.POST,request.FILES)
        print(mi_formulario)
        if mi_formulario.is_valid():
            titulo = mi_formulario.cleaned_data.get("titulo")
            subtitulo = mi_formulario.cleaned_data.get("subtitulo")
            cuerpo = mi_formulario.cleaned_data.get("cuerpo")
            autor = mi_formulario.cleaned_data.get("autor")
            imagen = mi_formulario.cleaned_data.get("imagen")
            obj = Camioneta.objects.create(titulo=titulo,subtitulo=subtitulo,cuerpo=cuerpo,autor=autor,imagen=imagen)
            obj.save()
            return redirect("camioneta")
    camionetas=Camioneta.objects.all()
    contexto = {
        "form" : CamionetaFormulario(),
        "camionetas" : camionetas,
    }
    return render(request,"agregar_camioneta.html",contexto)

@login_required
def camioneta_busqueda(request):
    contexto={
        "form":VehiculoBusqueda(),
    }
    return render(request,"camioneta_busqueda.html",contexto)

@login_required
def mostrar_camioneta(request):
    titulo=request.GET.get('titulo')
    camionetas=Camioneta.objects.filter(titulo__icontains=titulo)
    contexto={
        "camionetas":camionetas,
    }
    return render(request,"mostrar_camioneta.html",contexto)

@login_required
def ver_camioneta(request,titulo):
    camionetas=Camioneta.objects.filter(titulo__icontains=titulo)
    contexto={
        "camionetas":camionetas,
    }
    return render(request,"ver_camioneta.html",contexto)