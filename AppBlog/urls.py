from django.urls import path
from AppBlog import views

urlpatterns = [
    #auto
    path("autos/",views.auto,name="auto"),
    path("agregar_autos/",views.agregar_auto,name="agregarAuto"),
    path("auto_busqueda/",views.auto_busqueda,name="autoBusqueda"),
    path("mostrar_auto/",views.mostrar_auto,name="mostrarAuto"),
    path("agregar_imagen_auto",views.agregar_imagen_auto,name="agregarImagenAuto"),
    #moto
    path("motos/",views.moto,name="moto"),
    path("agregar_motos/",views.agregar_moto,name="agregarMoto"),
    path("moto_busqueda/",views.moto_busqueda,name="motoBusqueda"),
    path("mostrar_moto/",views.mostrar_moto,name="mostrarMoto"),
    path("agregar_imagen_motos",views.agregar_imagen_moto,name="agregarImagenMoto"),
    #camioneta
    path("camionetas/",views.camioneta,name="camioneta"),
    path("agregar_camionetas/",views.agregar_camioneta,name="agregarCamioneta"),
    path("camioneta_busqueda/",views.camioneta_busqueda,name="camionetaBusqueda"),
    path("mostrar_camioneta/",views.mostrar_camioneta,name="mostrarCamioneta"),
    path("agregar_imagen_camioneta",views.agregar_imagen_camioneta,name="agregarImagenCamioneta"),
]