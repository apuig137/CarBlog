from django.urls import path
from AppBlog import views

urlpatterns = [
    path("autos/",views.autos,name="auto"),
    path("auto_busqueda/",views.auto_busqueda,name="autoBusqueda"),
    path("auto_filtrado/",views.auto_filtrado,name="autoFiltrado"),
    #path("auto_formulario/",views.auto_formulario,name="autoFormulario"),
    path("motos/",views.moto,name="moto"),
    path("moto_formulario/",views.moto_formulario,name="motoFormulario"),    
    path("camionetas/",views.camioneta,name="camioneta"),
    path("camioneta_formulario/",views.camioneta_formulario,name="camionetaFormulario"),
]