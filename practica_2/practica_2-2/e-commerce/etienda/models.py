from django.db import models
from django.http import HttpResponse
from pymongo import MongoClient
import requests

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
print(f"Se insertaron {num_documentos} documentos desde la API.")


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

    return resultados_busqueda


# Obtener los productos de una categoría
def prods_categoria(categoria):
    resultados_categoria = productos_collection.find({"category": categoria})

    return resultados_categoria