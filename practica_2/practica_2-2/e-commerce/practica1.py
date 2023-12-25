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

# Especificaciones de la consulta
query_electronics = {
    'category': 'electronics',
    'price': {'$gte': 100, '$lte': 200} # $gte: greater than or equal, $lte: less than or equal
}

# Realizar la consulta
result_electronica = productos_collection.find(query_electronics).sort('price', -1) # -1: descending order

# Mostrar los resultados
print("\nProductos de electrónica entre 100 y 200€:")
for producto in result_electronica:
    print(producto['title'], "|", producto['price'], "€ |", producto['category'])



# 2. Productos que contengan la palabra 'pocket' en la descripción.
# --> Para más claridad muestra solo el nombre y la descripción

# Especificaciones de la consulta
query_pocket = {
    'description': {'$regex': 'pocket'} # $regex: regular expression
}

# Realizar la consulta
result_pocket = productos_collection.find(query_pocket)

# Mostrar los resultados
print("\nProductos con 'pocket' en la descripción:")
for producto in result_pocket:
    print(producto['title'], "|", producto['description'])


# 3. Productos con puntuación mayor de 4
# --> Para más claridad muestra solo el nombre, la puntuación y el número de votos

# Especificaciones de la consulta
query_rating = {
    'rating.rate': {'$gt': 4} # $gt: greater than
}

# Realizar la consulta
result_rating = productos_collection.find(query_rating)

# Mostrar los resultados
print("\nProductos con puntuación mayor de 4:")
for producto in result_rating:
    print(producto['title'], "|", producto['rating']['rate'], "(", producto['rating']['count'], "votos )")


# 4. Ropa de hombre, ordenada por puntuación
# --> Para más claridad muestra solo el nombre, la categoría y la puntuación

# Especificaciones de la consulta
query_men_clothing = {
    'category': "men's clothing"
}

# Realizar la consulta
result_men_clothing = productos_collection.find(query_men_clothing).sort('rating.rate', -1)

# Mostrar los resultados
print("\nRopa de hombre, ordenada por puntuación:")
for producto in result_men_clothing:
    print(producto['title'], "|", producto['category'], "|", producto['rating']['rate'])


# 5. Facturación total --> Suma de los precios de todos los productos

# Operaciones
total = Decimal(0.00) # Para evitar problemas de comas flotantes

for producto in productos_collection.find():
    precio = Decimal(str(producto['price'])) # Convertir a Decimal
    total += precio

# Mostrar el resultado
print("\nFacturación total:", total, "€")


# 6. Facturación por categoría de producto
# --> Muestra la categoría y la facturación total de la misma

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

# Mostrar los resultados
print("\nFacturación por categoría:")
for categoria, facturacion in facturacion_categorias.items():
    print(categoria, "|", facturacion, "€")