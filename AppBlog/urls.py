from django.urls import path
from AppBlog.views import *

urlpatterns = [
    #auto
    path("autos/",auto,name="auto"),
    path("eliminar_auto/<str:titulo>",eliminar_auto,name="eliminarAuto"),
    path("editar_auto/<str:titulo>",editar_auto,name="editarAuto"),
    path("agregar_autos/",agregar_auto,name="agregarAuto"),
    path("auto_busqueda/",auto_busqueda,name="autoBusqueda"),
    path("mostrar_auto/",mostrar_auto,name="mostrarAuto"),
    path("agregar_imagen_auto",agregar_imagen_auto,name="agregarImagenAuto"),
    #moto
    path("motos/",moto,name="moto"),
    path("eliminar_moto/<str:titulo>",eliminar_moto,name="eliminarMoto"),
    path("editar_moto/<str:titulo>",editar_moto,name="editarMoto"),
    path("agregar_motos/",agregar_moto,name="agregarMoto"),
    path("moto_busqueda/",moto_busqueda,name="motoBusqueda"),
    path("mostrar_moto/",mostrar_moto,name="mostrarMoto"),
    path("agregar_imagen_motos",agregar_imagen_moto,name="agregarImagenMoto"),
    #camioneta
    path("camionetas/",camioneta,name="camioneta"),
    path("eliminar_camioneta/<str:titulo>",eliminar_camioneta,name="eliminarCamioneta"),
    path("editar_camioneta/<str:titulo>",editar_camioneta,name="editarCamioneta"),
    path("agregar_camionetas/",agregar_camioneta,name="agregarCamioneta"),
    path("camioneta_busqueda/",camioneta_busqueda,name="camionetaBusqueda"),
    path("mostrar_camioneta/",mostrar_camioneta,name="mostrarCamioneta"),
    path("agregar_imagen_camioneta",agregar_imagen_camioneta,name="agregarImagenCamioneta"),
]