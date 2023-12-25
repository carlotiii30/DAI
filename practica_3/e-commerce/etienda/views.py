from django.http import HttpResponse
from etienda.models import *
from django.shortcuts import render
from etienda.forms import ProductoForm
from django.core.files.storage import default_storage


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


# Nuevo producto
def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            price = float(form.cleaned_data["price"])
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]
            category = form.cleaned_data["category"]

            nuevo_prod(title, price, description, image, category)

            return render(request, "index.html")

        else:
            logger.info(f"Formulario no valido")

    else:
        form = ProductoForm()

    return render(request, "nuevo_producto.html", {"form": form})
