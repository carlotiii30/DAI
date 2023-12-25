from pymongo import MongoClient
from django.conf import settings
import requests
import os
import logging

# Logger
logger = logging.getLogger(__name__)


# ---------------------------------------- CONEXION ----------------------------------------
# Conexión a la base de datos
client = MongoClient("mongo", 27017)
tienda_db = client.tienda
productos_collection = tienda_db.productos

api = "https://fakestoreapi.com/products"

# Vaciar la colección de productos existente
productos_collection.delete_many({})

# Obtener datos de la API
response = requests.get(api)
data = response.json()

# Insertar datos de la API en la base de datos
for item in data:
    # Asegurarse de que '_id' no esté presente en los datos API
    if "_id" in item:
        del item["_id"]

    # Insertar el documento en la colección de productos
    productos_collection.insert_one(item)

# Verificar la inserción
num_documentos = productos_collection.count_documents({})
logger.info(f"Productos insertados: {num_documentos}")

# ---------------------------------------- FUNCIONES ----------------------------------------


# Obtener todas las categorías
def obtener_categorias():
    categorias = productos_collection.distinct("category")

    return categorias


# Obtener todos los productos que contengan en el título una palabra
def busqueda(palabra):
    resultados_busqueda = productos_collection.find(
        {"title": {"$regex": palabra, "$options": "i"}}
    )

    logger.info(f"Busqueda realizada. Palabra: {palabra}")

    return resultados_busqueda


# Obtener los productos de una categoría
def prods_categoria(categoria):
    resultados_categoria = productos_collection.find({"category": categoria})

    logger.info(f"Productos de una categoria obtenidos. Categoria: {categoria}")

    return resultados_categoria


# Crear un producto
def nuevo_prod(title, price, description, image, category):
    nombre_imagen = guardar_imagen(image, title)
    url = url_imagen(nombre_imagen)

    producto = {
        "title": title,
        "price": price,
        "description": description,
        "image": url,
        "category": category,
    }

    productos_collection.insert_one(producto)

    logger.info("Producto creado")


# Guardar una imagen en el directorio 'media'
def guardar_imagen(imagen, nombre):
    nombre_imagen = str(nombre) + ".jpg"
    ruta = os.path.join(settings.MEDIA_ROOT, nombre_imagen)

    with open(ruta, "wb+") as destino:
        for chunk in imagen.chunks():
            destino.write(chunk)

    logger.info("Imagen guardada")

    return nombre_imagen



# url de la imagen
def url_imagen(nombre):
    url = settings.MEDIA_URL

    return f"{url}{nombre}"
