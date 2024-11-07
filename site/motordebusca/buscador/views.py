from django.shortcuts import render, HttpResponse
from .models import Pontos

# Create your views here.
def index(req):
    #pontos = {"pontos": Pontos.objects.all() }  
    #resultados = "São Paulo"
    return render(req, "buscador/index.html")

def resultados(req):
    pontos = Pontos.objects.all()
    cidade = req.POST.get('cidade')
    filtrados = ""
    if cidade == "": 
        filtrados = { "pontos":  pontos }
    else: 
        filtrados = { "pontos":  [obj for obj in pontos if obj.cidade == cidade] }
     
    return render(req, "buscador/resultados.html", filtrados)

def david(req):
    return render(req, "buscador/david.html")


def roberto(req):
    return render(req, "buscador/david.html")
    #return HttpResponse("Boa tarde")