from django.db import models
from django.http import HttpResponse
from pymongo import MongoClient
import requests
from decimal import Decimal

# Conexión a la base de datos
client = MongoClient('mongo', 27017)
tienda_db = client.tienda
productos_collection = tienda_db.productos

api = 'https://fakestoreapi.com/products'

# Vaciar la colección de productos existente
productos_collection.delete_many({})

# Obtener datos de la API
response = requests.get(api)
data = response.json()

# Insertar datos de la API en la base de datos
for item in data:
    # Asegurarse de que '_id' no esté presente en los datos API
    if '_id' in item:
        del item['_id']

    # Insertar el documento en la colección de productos
    productos_collection.insert_one(item)

# Verificar la inserción
num_documentos = productos_collection.count_documents({})
print(f"Se insertaron {num_documentos} documentos desde la API.")


## - - - - - - - - - CONSULTAS - - - - - - - - - ##

# 1. Electrónica entre 100 y 200€, ordenados por precio.
# --> Para más claridad muestra solo el nombre, el precio y la categoría
def consulta1():
    # Especificaciones de la consulta
    query_electronics = {
        'category': 'electronics',
        'price': {'$gte': 100, '$lte': 200} # $gte: greater than or equal, $lte: less than or equal
    }

    # Realizar la consulta
    result_electronica = productos_collection.find(query_electronics).sort('price', -1) # -1: descending order

    # Guardar los resultados
    respuesta = "<h3>Productos de electrónica entre 100 y 200€: </h3>"
    for producto in result_electronica:
        respuesta += f"Titulo: {producto['title']} <br>"
        respuesta += f"Precio: {producto['price']} € <br>"
        respuesta += f"Categoría: {producto['category']} <br> <br>"

    return respuesta


# 2. Productos que contengan la palabra 'pocket' en la descripción.
# --> Para más claridad muestra solo el nombre y la descripción
def consulta2():
    # Especificaciones de la consulta
    query_pocket = {
        'description': {'$regex': 'pocket'} # $regex: regular expression
    }

    # Realizar la consulta
    result_pocket = productos_collection.find(query_pocket)

    # Guardar los resultados
    respuesta = "<h3>Productos con 'pocket' en la descripción: </h3>"
    for producto in result_pocket:
        respuesta += f"Titulo: {producto['title']} <br>"
        respuesta += f"Descripción: {producto['description']} <br> <br>"

    return respuesta


# 3. Productos con puntuación mayor de 4
# --> Para más claridad muestra solo el nombre, la puntuación y el número de votos
def consulta3():
    # Especificaciones de la consulta
    query_rating = {
        'rating.rate': {'$gt': 4} # $gt: greater than
    }

    # Realizar la consulta
    result_rating = productos_collection.find(query_rating)

    # Guardar los resultados
    respuesta = "<h3> Productos con puntuación mayor de 4: </h3>"
    for producto in result_rating:
        respuesta += f"Titulo: {producto['title']} <br>"
        respuesta += f"Puntuación: {producto['rating']['rate']} <br>"
        respuesta += f"Votos: {producto['rating']['count']} <br> <br>"

    return respuesta


# 4. Ropa de hombre, ordenada por puntuación
# --> Para más claridad muestra solo el nombre, la categoría y la puntuación
def consulta4():
    # Especificaciones de la consulta
    query_men_clothing = {
        'category': "men's clothing"
    }

    # Realizar la consulta
    result_men_clothing = productos_collection.find(query_men_clothing).sort('rating.rate', -1)

    # Mostrar los resultados
    respuesta = "<h3> Ropa de hombre, ordenada por puntuación: </h3>"
    for producto in result_men_clothing:
        respuesta += f"Titulo: {producto['title']} <br>"
        respuesta += f"Categoría: {producto['category']} <br>"
        respuesta += f"Puntuación: {producto['rating']['rate']} <br> <br>"

    return respuesta


# 5. Facturación total --> Suma de los precios de todos los productos
def consulta5():
    # Operaciones
    total = Decimal(0.00) # Para evitar problemas de comas flotantes

    for producto in productos_collection.find():
        precio = Decimal(str(producto['price'])) # Convertir a Decimal
        total += precio

    # Guardar el resultado
    respuesta = "Facturación total: ", total, "€"

    return respuesta


# 6. Facturación por categoría de producto
# --> Muestra la categoría y la facturación total de la misma
def consulta6():
    # Diccionario para guardar los resultados parciales
    facturacion_categorias = {}

    # Operaciones
    for producto in productos_collection.find():
        categoria = producto['category']
        precio = Decimal(str(producto['price']))

        # Si la categoría no está en el diccionario, se crea
        if categoria not in facturacion_categorias:
            facturacion_categorias[categoria] = Decimal(0.00)
        # Si la categoría está en el diccionario, se suma el precio
        else:
            facturacion_categorias[categoria] += precio

    # Guardar los resultados
    respuesta = "<h3> Facturación por categoría: </h3>"
    for categoria, facturacion in facturacion_categorias.items():
        respuesta += f"\n{categoria} | {facturacion} € <br>"

    return respuesta