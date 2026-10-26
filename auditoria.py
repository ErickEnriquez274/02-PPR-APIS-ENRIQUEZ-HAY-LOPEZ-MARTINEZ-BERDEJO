import requests
import json

try:
    respuesta = requests.get(
        "https://dummyjson.com/carts",
        params={"limit": 0},
        timeout=15
    )
except requests.exceptions.RequestException as error:
    raise SystemExit(f"No se pudo conectar con la API: {error}")

if respuesta.status_code != 200:
    raise SystemExit(
        f"Error al consultar carritos: HTTP {respuesta.status_code}"
    )

datos = respuesta.json()

#PARTE DEL DESARROLLADOR 2. HAY MARTINEZ JUAN PABLO

carritos = datos["carts"]

print(json.dumps(carritos, indent=4, ensure_ascii=False))


totales = []
total_general = 0

for carrito in carritos:
    cantidad_valida = 0

    for producto in carrito["products"]:
        if producto["discountPercentage"] < 12:
            cantidad_valida += producto["quantity"]

    totales.append({
        "carritoId": carrito["id"],
        "userId": carrito["userId"],
        "cantidad": cantidad_valida
    })

    total_general += cantidad_valida

    print(
        f"Carrito {carrito['id']}: "
        f"{cantidad_valida} unidades válidas"
    )

print("=" * 50)
print(f"Total general: {total_general} unidades válidas")

#PARTE  FINAL DEL DESARROLLADOR 2. HAY MARTINEZ JUAN PABLO

id_carrito = 20
id_usuario = 17
mayor_cantidad = 16

# Construir la URL con el ID del usuario.
url_usuario = f"https://dummyjson.com/users/{id_usuario}"

# Ejecutar la segunda petición.
try:
    respuesta_usuario = requests.get(
        url_usuario,
        timeout=15
    )
except requests.exceptions.RequestException as error:
    raise SystemExit(f"Error de conexión: {error}")

# Validar el estado HTTP.
if respuesta_usuario.status_code != 200:
    raise SystemExit(
        f"Error al consultar usuario: HTTP "
        f"{respuesta_usuario.status_code}"
    )

# Obtener los datos del usuario.
usuario = respuesta_usuario.json()

print("ID del carrito:", id_carrito)
print("ID del usuario:", id_usuario)
print("Máximo de unidades válidas:", mayor_cantidad)
print("URL consultada:", url_usuario)
print("Datos del usuario:", usuario)