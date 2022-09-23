from django.urls import path
from AppUsuario.views import *

urlpatterns = [
    path("signup/",signup,name="signup")
]