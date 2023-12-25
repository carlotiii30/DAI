from django.http import HttpResponse
from etienda.models import *
from django.shortcuts import render


# Indice de la tienda
def index(request):
    categorias = (
        obtener_categorias()
    )  # Obtener la lista de categorías desde la base de datos

    return render(request, "index.html", {"categorias": categorias})


# Busqueda
def resultado_busqueda(request):
    if request.method == "GET":
        palabra_a_buscar = request.GET.get(
            "q", " "
        )  # Si no hay nada en 'q', devuelve ' '
        resultados = busqueda(palabra_a_buscar)  # Buscar en la base de datos

        return render(
            request,
            "busqueda.html",
            {"resultados": resultados, "palabra_a_buscar": palabra_a_buscar},
        )


# Categoria
def categorias(request, categoria):
    resultados = prods_categoria(categoria)

    return render(
        request, "categorias.html", {"resultados": resultados, "categoria": categoria}
    )