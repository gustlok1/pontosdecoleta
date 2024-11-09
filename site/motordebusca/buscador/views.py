from django.shortcuts import render, HttpResponse
from .models import Pontos
from unidecode import unidecode

def padronizar_string(texto):
    texto = texto.lower()
    texto = unidecode(texto)
    return texto

# Create your views here.
def index(req):
    #pontos = {"pontos": Pontos.objects.all() }  
    #resultados = "São Paulo"
    return render(req, "buscador/index.html")

def resultados(req):
    pontos = Pontos.objects.all()
    cidade = req.POST.get('cidade')
    response = {}
    if cidade == "": 
        response["pontos"] =  pontos
        response["searched_city"] =  cidade
    else: 
        response = { "pontos":  [obj for obj in pontos if padronizar_string(cidade) in padronizar_string(obj.cidade)] }
        response["searched_city"] =  cidade
     
    return render(req, "buscador/resultados.html", response)

def david(req):
    return render(req, "buscador/david.html")


def roberto(req):
    return render(req, "buscador/david.html")
    #return HttpResponse("Boa tarde")