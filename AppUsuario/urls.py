from django.urls import path
from AppUsuario.views import *

urlpatterns = [
    path("signup/",signup,name="signup"),
    path("editar_perfil/",editar_perfil,name="editarPerfil"),
    path("editar_avatar",editar_avatar,name="editarAvatar"),
    path("agregar_avatar",agregar_avatar,name="agregarAvatar"),
]