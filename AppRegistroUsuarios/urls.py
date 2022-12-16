from django.urls import path
from AppRegistroUsuarios.views import *

urlpatterns = [
    path ("", inicio, name = "inicio"),
    path ("registro/", registro_usuario, name = "registro_usuario"),
    path ("ingreso/", Pagina_de_ingreso, name = "Pagina_de_ingreso" ),

]