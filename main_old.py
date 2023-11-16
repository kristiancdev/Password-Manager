import getpass
import json

def crear_gestor_contraseñas():
    try:
        with open('contraseñas.json', 'r') as archivo:
            gestor_contraseñas = json.load(archivo)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        gestor_contraseñas = {}

    return gestor_contraseñas

def guardar_gestor_contraseñas(gestor_contraseñas):
    with open('contraseñas.json', 'w') as archivo:
        json.dump(gestor_contraseñas, archivo, indent=2)

def agregar_contraseña():
    sitio = input("Ingrese el nombre del sitio o servicio: ")
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")

    gestor_contraseñas = crear_gestor_contraseñas()
    gestor_contraseñas[sitio] = {"usuario": usuario, "contraseña": contraseña}
    guardar_gestor_contraseñas(gestor_contraseñas)
    print(f"Contraseña para {sitio} agregada con éxito.")

def obtener_contraseña():
    sitio = input("Ingrese el nombre del sitio o servicio: ")

    gestor_contraseñas = crear_gestor_contraseñas()
    if sitio in gestor_contraseñas:
        usuario = gestor_contraseñas[sitio]["usuario"]
        contraseña = gestor_contraseñas[sitio]["contraseña"]
        print(f"Usuario: {usuario}\nContraseña: {contraseña}")
    else:
        print(f"No se encontró la contraseña para {sitio}.")

# Ejemplo de uso
while True:
    print("\n1. Agregar Contraseña\n2. Obtener Contraseña\n3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_contraseña()
    elif opcion == "2":
        obtener_contraseña()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Intente de nuevo.")
