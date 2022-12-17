from django.urls import path
from AppRegistroUsuarios.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ("", inicio, name = "inicio"),
    path ("registro/", registro_usuario, name = "registro_usuario"),
    path ("ingreso/", Pagina_de_ingreso, name = "Pagina_de_ingreso" ),
    path("desconectarse/", desconectarse, name = "desconectarse" ),
    path("prueba/", prueba),

]