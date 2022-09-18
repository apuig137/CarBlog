from ast import AugStore
from distutils.command.upload import upload
from msilib.schema import Class
from multiprocessing import current_process
from django.db import models

class Auto(models.Model):
    titulo=models.CharField(max_length=30, unique=True)
    subtitulo=models.CharField(max_length=50)
    cuerpo=models.CharField(max_length=500)
    autor=models.CharField(max_length=20)
    fecha=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.titulo
        

class Moto(models.Model):
    titulo=models.CharField(max_length=30, unique=True)
    subtitulo=models.CharField(max_length=50)
    cuerpo=models.CharField(max_length=500)
    autor=models.CharField(max_length=20)
    fecha=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.titulo


class Camioneta(models.Model):
    titulo=models.CharField(max_length=30, unique=True)
    subtitulo=models.CharField(max_length=50)
    cuerpo=models.CharField(max_length=500)
    autor=models.CharField(max_length=20)
    fecha=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.titulo


class AutoImagen(models.Model):
    auto=models.OneToOneField(Auto, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="autos",null=True)
    def __str__(self):
        return self.auto


class MotoImagen(models.Model):
    moto=models.OneToOneField(Moto, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="motos",null=True)
    def __str__(self):
        return self.moto


class CamionetaImagen(models.Model):
    camioneta=models.OneToOneField(Camioneta, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="camionetas",null=True)
    def __str__(self):
        return self.camioneta
