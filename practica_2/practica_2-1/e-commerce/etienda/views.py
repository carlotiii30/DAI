from django.http import HttpResponse
from etienda.models import *


# Indice de la tienda
def index(request):
    respuesta = "<h2>Índice de Consultas:</h2>"
    respuesta += '<a href="/etienda/consulta1">1. Electrónica entre 100 y 200€, ordenados por precio</a><br>'
    respuesta += '<a href="/etienda/consulta2">2. Productos que contengan la palabra pocket en la descripción</a><br>'
    respuesta += '<a href="/etienda/consulta3">3. Productos con puntuación mayor de 4</a><br>'
    respuesta += '<a href="/etienda/consulta4">4. Ropa de hombre, ordenada por puntuación</a><br>'
    respuesta += '<a href="/etienda/consulta5">5. Facturación total</a><br>'
    respuesta += '<a href="/etienda/consulta6">6. Facturación por categoría</a><br>'

    return HttpResponse(respuesta)

def primera_consulta(request):
    respuesta = consulta1()
    return HttpResponse(respuesta)

def segunda_consulta(request):
    respuesta = consulta2()
    return HttpResponse(respuesta)

def tercera_consulta(request):
    respuesta = consulta3()
    return HttpResponse(respuesta)

def cuarta_consulta(request):
    respuesta = consulta4()
    return HttpResponse(respuesta)

def quinta_consulta(request):
    respuesta = consulta5()
    return HttpResponse(respuesta)

def sexta_consulta(request):
    respuesta = consulta6()
    return HttpResponse(respuesta)