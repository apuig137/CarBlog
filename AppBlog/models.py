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
    fecha=models.DateField()
    imagen=models.ImageField(upload_to="media", null=True)

class Moto(models.Model):
    titulo=models.CharField(max_length=30, unique=True)
    subtitulo=models.CharField(max_length=50)
    cuerpo=models.CharField(max_length=500)
    autor=models.CharField(max_length=20)
    fecha=models.DateField()
    imagen=models.ImageField(upload_to="media", null=True)

class Camioneta(models.Model):
    titulo=models.CharField(max_length=30, unique=True)
    subtitulo=models.CharField(max_length=50)
    cuerpo=models.CharField(max_length=500)
    autor=models.CharField(max_length=20)
    fecha=models.DateField()
    imagen=models.ImageField(upload_to="media", null=True)