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