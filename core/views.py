from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
from core.models import Evento


# def index(request):
#    return redirect('/agenda')


def buscar_evento(request, titulo_evento):
    teste = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('<h1>O local do evento é em {}</h1>'.format(teste.local))


@login_required(login_url='/login/')
def listar_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {"eventos": evento}
    return render(request, 'agenda.html', dados)


def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Login está errado')

    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')
