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
#PARTE INICIAL DEL DESARROLLADOR 3. LOPEZ BERMON DIEGO DE JESUS

id_carrito = 20
id_usuario = 17
mayor_cantidad = 16


url_usuario = f"https://dummyjson.com/users/{id_usuario}"


try:
    respuesta_usuario = requests.get(
        url_usuario,
        timeout=15
    )
except requests.exceptions.RequestException as error:
    raise SystemExit(f"Error de conexión: {error}")


if respuesta_usuario.status_code != 200:
    raise SystemExit(
        f"Error al consultar usuario: HTTP "
        f"{respuesta_usuario.status_code}"
    )

usuario = respuesta_usuario.json()

print("ID del carrito:", id_carrito)
print("ID del usuario:", id_usuario)
print("Máximo de unidades válidas:", mayor_cantidad)
print("URL consultada:", url_usuario)
print("Datos del usuario:", usuario)

#PARTE FINAL DEL DESARROLLADOR 3. LOPEZ BERMON DIEGO DE JESUS

#PARTE INICIAL DEL DESARROLLADOR 4. MARTINEZ DE DIOS SONIA, BERDEJO SALAS GEORGETTE
# Extraer los datos del usuario.
nombre = usuario["firstName"]
apellido = usuario["lastName"]
ciudad = usuario["address"]["city"]

# Construir el mensaje solicitado.
mensaje = (
    f"El cliente con más productos regulares es "
    f"{nombre} {apellido} (ID: {id_usuario}), "
    f"de la ciudad de {ciudad}. "
    f"Compró un total de {mayor_cantidad} productos válidos."
)

# Preparar el reporte con separadores.
separador = "=" * 70
reporte = f"{separador}\n{mensaje}\n{separador}\n"

# Mostrar el reporte en consola.
print(reporte, end="")

# Guardar el mismo reporte en el archivo.
with open("reporte_auditoria.txt", "w", encoding="utf-8") as archivo:
    archivo.write(reporte)

# PARTE FINAL DEL DESARROLLADOR 4. MARTINEZ DE DIOS SONIA, BERDEJO SALAS GEORGETTE