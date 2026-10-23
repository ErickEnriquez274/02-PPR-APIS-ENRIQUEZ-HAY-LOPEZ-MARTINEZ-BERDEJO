import requests

# Obtener todos los carritos.
try:
    respuesta = requests.get(
        "https://dummyjson.com/carts",
        params={"limit": 0},
        timeout=15
    )
except requests.exceptions.RequestException as error:
    raise SystemExit(f"No se pudo conectar con la API: {error}")

# Validar el estado HTTP antes de usar los datos.
if respuesta.status_code != 200:
    raise SystemExit(
        f"Error al consultar carritos: HTTP {respuesta.status_code}"
    )

# Convertir la respuesta JSON a datos de Python.
datos = respuesta.json()

# Extraer la lista de carritos.
carritos = datos["carts"]
print("Carritos descargados:", len(carritos))
print("Total indicado por la API:", datos["total"])