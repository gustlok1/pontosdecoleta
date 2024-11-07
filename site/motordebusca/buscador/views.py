from django.shortcuts import render, HttpResponse
from .models import Pontos

# Create your views here.
def index(req):
    pontos = {"pontos": Pontos.objects.all() }  
    resultados = "São Paulo"
    return render(req, "buscador/index.html", pontos )
def david(req):
    return render(req, "buscador/david.html")
    #return HttpResponse("Boa tarde")