from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from AppBlog.models import *
from AppBlog.forms import *
import datetime

def inicio(request):
    return render(request,"index.html")

def moto(request):
    return render(request,"moto.html")

def camioneta(request):
    return render(request,"camioneta.html")

def autos(request):
    if request.method == "POST":
        mi_formulario = AutoFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            auto1=Auto(titulo=data.get("titulo"),subtitulo=data.get("subtitulo"),cuerpo=data.get("cuerpo"),autor=data.get("autor"),fecha=data.get("fecha"),imagen=data.get("imagen"))
            auto1.save()
            return redirect("auto")
    autos=Auto.objects.all()
    contexto = {
        "form" : AutoFormulario(),
        "autos" : autos,
    }
    return render(request,"auto.html",contexto)

def auto_busqueda(request):
    contexto = {
        "form" : VehiculoBusqueda(),
    } 
    return render(request,"auto_busqueda.html",contexto)

def auto_filtrado(request):
    titulo = request.GET.get("titulo")
    autos = Auto.objects.filter(titulo__icontains=titulo)
    contexto = {
        "autos" : autos,
    }
    return render(request,"auto_filtrado.html",contexto)

def moto_formulario(request):
    contexto = {
        "form" : MotoFormulario()
    }
    return render(request,"moto_formulario.html",contexto)

def camioneta_formulario(request):
    contexto = {
        "form" : CamionetaFormulario()
    }
    return render(request,"camioneta_formulario.html",contexto)