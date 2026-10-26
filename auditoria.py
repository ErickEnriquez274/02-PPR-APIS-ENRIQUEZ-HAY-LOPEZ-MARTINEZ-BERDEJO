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