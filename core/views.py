from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# Create your views here.
from core.models import Evento


def buscar_evento(request, titulo_evento):
    teste = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('<h1>O local do evento é em {}</h1>'.format(teste.local))