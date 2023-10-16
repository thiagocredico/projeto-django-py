from django.shortcuts import render, redirect
from .models import Usuario

# Create your views here.


def home(request):
    return render(request, "usuarios/home.html")


def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get("nome")
    novo_usuario.idade = request.POST.get("idade")
    if novo_usuario.nome:
        novo_usuario.save()

    usuarios = {
        "usuarios": Usuario.objects.all()
    }

    return render(request, "usuarios/usuarios.html", usuarios)


def editar(request, id):
    usuario = Usuario.objects.get(id_usuario=id)
    return render(request, "usuarios/update.html", {"usuario": usuario})


def update(request, id):
    novo_nome = request.POST.get("nome")
    nova_idade = request.POST.get("idade")
    usuario = Usuario.objects.get(id_usuario=id)
    usuario.nome = novo_nome
    usuario.idade = nova_idade
    usuario.save()
    return redirect("/usuarios/")
