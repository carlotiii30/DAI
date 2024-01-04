from pymongo import MongoClient
from django.conf import settings
import requests
import os
import logging
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

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
num_documentos = productos_collection.estimated_document_count()
logger.info(f"Productos insertados: {num_documentos}")

# ---------------------------------------- FUNCIONES ----------------------------------------


# Obtener todas las categorías
def obtener_categorias():
    categorias = productos_collection.distinct("category")

    return categorias


# Obtener todos los productos que contengan en el título o en la descripción una palabra
def busqueda(palabra):
    resultados_busqueda = productos_collection.find(
        {"$or": [{"title": {"$regex": palabra}}, {"description": {"$regex": palabra}}]}
    )

    productos = list(resultados_busqueda)

    for producto in productos:
        producto["id"] = str(producto.get("_id"))
        del producto["_id"]

    logger.info(f"Resultados de la busqueda obtenidos. Palabra: {palabra}")

    return productos


# Obtener los productos de una categoría
def prods_categoria(categoria):
    resultados_categoria = productos_collection.find({"category": categoria})

    productos = list(resultados_categoria)

    for producto in productos:
        producto["id"] = str(producto.get("_id"))
        del producto["_id"]

    logger.info(f"Productos de una categoria obtenidos. Categoria: {categoria}")

    return productos


# Crear un producto
def nuevo_prod(title, price, description, image, category):
    nombre_imagen = guardar_imagen(image, title)
    url = url_imagen(nombre_imagen)

    producto = {
        "title": title,
        "price": float(price),
        "description": description,
        "image": url,
        "category": category,
    }

    productos_collection.insert_one(producto)

    logger.info("Producto creado: " + str(producto))


# Guardar una imagen en el directorio 'media'
def guardar_imagen(imagen, nombre):
    try:
        nombre_imagen = default_storage.save(
            os.path.join(settings.MEDIA_ROOT, nombre), ContentFile(imagen.read())
        )

        logger.info("Imagen guardada")
        return nombre_imagen
    except Exception as e:
        logger.error(f"Error al guardar la imagen: {str(e)}")
        return None


# url de la imagen
def url_imagen(nombre):
    url = settings.MEDIA_URL

    if not url.endswith("/"):
        url += "/"

    return f"{url}{nombre}"
