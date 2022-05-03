from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse

# Create your views here.
from core.models import Evento

#def index(request):
#    return redirect('/agenda')

def buscar_evento(request, titulo_evento):
    teste = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('<h1>O local do evento é em {}</h1>'.format(teste.local))


def listar_eventos(request):
    evento = Evento.objects.all()
    dados = {"eventos": evento}
    return render(request, 'agenda.html', dados)