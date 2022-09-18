from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppBlog.models import *
from AppBlog.forms import *


def inicio(request):
    return render(request,"index.html")


def auto(request):
    if request.method == "POST":
        mi_formulario = AutoFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            titulo = mi_formulario.cleaned_data.get("titulo")
            subtitulo = mi_formulario.cleaned_data.get("subtitulo")
            cuerpo = mi_formulario.cleaned_data.get("cuerpo")
            autor = mi_formulario.cleaned_data.get("autor")
            obj = Auto.objects.create(titulo = titulo,subtitulo = subtitulo,cuerpo =cuerpo,autor=autor)
            obj.save()
            return redirect("auto")
    autos=Auto.objects.all()
    contexto = {
        "form" : AutoFormulario(),
        "autos" : autos,
    }
    return render(request,"auto.html",contexto)


def auto_filtrado(request):
    titulo = request.GET.get("titulo")
    autos = Auto.objects.filter(titulo__icontains=titulo)
    contexto = {
        "autos" : autos,
    }
    return render(request,"auto_filtrado.html",contexto)


def agregar_imagen_auto(request):
    if request.method=="POST":
        mi_formulario=AutoImagenFormulario(request.POST,request.FILES)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            foto=AutoImagen.objects.filter(auto=data.get("titulo"))
            if len(foto)>0:
                foto=foto[0]
                foto.imagen=mi_formulario.cleaned_data["imagen"]
                foto.save()
            else:
                foto=AutoImagen(auto=data.get("auto"), imagen=data.get("imagen"))
                foto.save()
        return redirect("inicio")
    contexto={
        "form":AutoImagenFormulario(),
    }
    return render(request,"agregar_imagen_auto.html",contexto)


def moto(request):
    if request.method == "POST":
        mi_formulario = MotoFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            titulo = mi_formulario.cleaned_data.get("titulo")
            subtitulo = mi_formulario.cleaned_data.get("subtitulo")
            cuerpo = mi_formulario.cleaned_data.get("cuerpo")
            autor = mi_formulario.cleaned_data.get("autor")
            obj = Moto.objects.create(titulo = titulo,subtitulo = subtitulo,cuerpo =cuerpo,autor=autor)
            obj.save()
            return redirect("camioneta")
    motos=Moto.objects.all()
    contexto = {
        "form" : MotoFormulario(),
        "motos" : motos,
    }
    return render(request,"moto.html",contexto)


def moto_filtrado(request):
    titulo = request.GET.get("titulo")
    motos = Moto.objects.filter(titulo__icontains=titulo)
    contexto = {
        "motos" : motos,
    }
    return render(request,"moto_filtrado.html",contexto)


def agregar_imagen_moto(request):
    if request.method=="POST":
        mi_formulario=MotoImagenFormulario(request.POST,request.FILES)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            foto=MotoImagen.objects.filter(auto=data.get("titulo"))
            if len(foto)>0:
                foto=foto[0]
                foto.imagen=mi_formulario.cleaned_data["imagen"]
                foto.save()
            else:
                foto=MotoImagen(auto=data.get("auto"), imagen=data.get("imagen"))
                foto.save()
        return redirect("inicio")
    contexto={
        "form":MotoImagenFormulario(),
    }
    return render(request,"agregar_imagen_moto.html",contexto)


def camioneta(request):
    if request.method == "POST":
        mi_formulario = CamionetaFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            titulo = mi_formulario.cleaned_data.get("titulo")
            subtitulo = mi_formulario.cleaned_data.get("subtitulo")
            cuerpo = mi_formulario.cleaned_data.get("cuerpo")
            autor = mi_formulario.cleaned_data.get("autor")
            obj = Camioneta.objects.create(titulo = titulo,subtitulo = subtitulo,cuerpo =cuerpo,autor=autor)
            obj.save()
            return redirect("camioneta")
    camionetas=Camioneta.objects.all()
    contexto = {
        "form" : CamionetaFormulario(),
        "camionetas" : camionetas,
    }
    return render(request,"camioneta.html",contexto)


def camioneta_filtrado(request):
    titulo = request.GET.get("titulo")
    camionetas = Camioneta.objects.filter(titulo__icontains=titulo)
    contexto = {
        "camionetas" : camionetas,
    }
    return render(request,"camioneta_filtrado.html",contexto)


def agregar_imagen_camioneta(request):
    if request.method=="POST":
        mi_formulario=CamionetaImagenFormulario(request.POST,request.FILES)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            foto=CamionetaImagen.objects.filter(auto=data.get("titulo"))
            if len(foto)>0:
                foto=foto[0]
                foto.imagen=mi_formulario.cleaned_data["imagen"]
                foto.save()
            else:
                foto=CamionetaImagen(auto=data.get("auto"), imagen=data.get("imagen"))
                foto.save()
        return redirect("inicio")
    contexto={
        "form":CamionetaImagenFormulario(),
    }
    return render(request,"agregar_imagen_camioneta.html",contexto)



def busqueda(request):
    contexto = {
        "form" : VehiculoBusqueda(),
    } 
    return render(request,"busqueda.html",contexto)