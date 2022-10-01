from django.db import models

class Auto(models.Model):
    titulo=models.CharField(max_length=30, unique=True)
    subtitulo=models.CharField(max_length=50)
    cuerpo=models.CharField(max_length=1000)
    autor=models.CharField(max_length=20)
    fecha=models.DateField(auto_now_add=True)
    imagen=models.ImageField(upload_to="autos",null=True)
    def __str__(self):
        return self.titulo
        
class Moto(models.Model):
    titulo=models.CharField(max_length=30, unique=True)
    subtitulo=models.CharField(max_length=50)
    cuerpo=models.CharField(max_length=1000)
    autor=models.CharField(max_length=20)
    fecha=models.DateField(auto_now_add=True)
    imagen=models.ImageField(upload_to="motos",null=True)
    def __str__(self):
        return self.titulo

class Camioneta(models.Model):
    titulo=models.CharField(max_length=30, unique=True)
    subtitulo=models.CharField(max_length=50)
    cuerpo=models.CharField(max_length=1000)
    autor=models.CharField(max_length=20)
    fecha=models.DateField(auto_now_add=True)
    imagen=models.ImageField(upload_to="camionetas",null=True)
    def __str__(self):
        return self.titulo
