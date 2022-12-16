from django.shortcuts import render
from django.contrib.auth import login, authenticate
from AppRegistroUsuarios.registroForm import CrearUsuario
from django.contrib.auth.forms import AuthenticationForm

def inicio(request):
    return render (request, "Inicio.html")

#--- Pagina de registro---#

def registro_usuario(request):
    if request.method=="POST":
        form=CrearUsuario(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request, "registro_usuario.html")
    else:
        form = CrearUsuario()
    return render(request, 'registro_usuario.html',{"form":form})

#--- Login ---#

def Pagina_de_ingreso(request):
    if request.method == "POST":
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            nombreusuario = form.cleaned_data.get["username"]
            claveusuario = form.cleaned_data.get["password"]
            usuario = authenticate (username=nombreusuario, password=claveusuario)
            if usuario is not None:
                Pagina_de_ingreso (request, usuario)
                return render (request, "inicio.html")
            else:
                return render (request, "Pagina_de_ingreso.html")
        else:
            return render (request, "Pagina_de_ingreso.html")
    else:
        form=AuthenticationForm()
    
    return render (request, "Pagina_de_ingreso.html")

            



