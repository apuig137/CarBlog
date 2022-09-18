from django.urls import path
from AppBlog import views

urlpatterns = [
    path("autos/",views.auto,name="auto"),
    path("auto_filtrado/",views.auto_filtrado,name="autoFiltrado"),
    path("agregar_imagen_auto",views.agregar_imagen_auto,name="agregarImagenAuto"),
    path("motos/",views.moto,name="moto"),
    path("moto_filtrado/",views.moto_filtrado,name="motoFiltrado"),
    path("agregar_imagen_moto",views.agregar_imagen_moto,name="agregarImagenMoto"),
    path("camionetas/",views.camioneta,name="camioneta"),
    path("camioneta_filtrado/",views.camioneta_filtrado,name="camionetaFiltrado"),
    path("agregar_imagen_camioneta",views.agregar_imagen_camioneta,name="agregarImagenCamioneta"),
    path("busqueda/",views.busqueda,name="busqueda"),
]