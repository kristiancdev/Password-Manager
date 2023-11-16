import hashlib
from cryptography.fernet import Fernet
import getpass
import json


# Genera una clave para cifrar/descifrar contraseñas
def generar_clave_maestra(password):
    salt = b'salt_unico_para_cada_usuario'  # Cambia esto por un valor único
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key

# Cifra una cadena de texto
def cifrar_texto(texto, clave):
    cipher_suite = Fernet(clave)
    cifrado = cipher_suite.encrypt(texto.encode('utf-8'))
    return cifrado

# Descifra una cadena de texto
def descifrar_texto(cifrado, clave):
    cipher_suite = Fernet(clave)
    texto = cipher_suite.decrypt(cifrado).decode('utf-8')
    return texto

def crear_gestor_contraseñas(clave_maestra):
    try:
        with open('contraseñas.json', 'rb') as archivo:
            gestor_contraseñas_cifrado = archivo.read()
            gestor_contraseñas = descifrar_texto(gestor_contraseñas_cifrado, clave_maestra)
            gestor_contraseñas = json.loads(gestor_contraseñas)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        gestor_contraseñas = {}

    return gestor_contraseñas

def guardar_gestor_contraseñas(gestor_contraseñas, clave_maestra):
    gestor_contraseñas_cifrado = cifrar_texto(json.dumps(gestor_contraseñas), clave_maestra)
    with open('contraseñas.json', 'wb') as archivo:
        archivo.write(gestor_contraseñas_cifrado)

def agregar_contraseña(clave_maestra):
    sitio = input("Ingrese el nombre del sitio o servicio: ")
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")

    gestor_contraseñas = crear_gestor_contraseñas(clave_maestra)
    gestor_contraseñas[sitio] = {"usuario": usuario, "contraseña": contraseña}
    guardar_gestor_contraseñas(gestor_contraseñas, clave_maestra)
    print(f"Contraseña para {sitio} agregada con éxito.")

def obtener_contraseña(clave_maestra):
    sitio = input("Ingrese el nombre del sitio o servicio: ")

    gestor_contraseñas = crear_gestor_contraseñas(clave_maestra)
    if sitio in gestor_contraseñas:
        usuario = gestor_contraseñas[sitio]["usuario"]
        contraseña = gestor_contraseñas[sitio]["contraseña"]
        print(f"Usuario: {usuario}\nContraseña: {contraseña}")
    else:
        print(f"No se encontró la contraseña para {sitio}.")

# Autenticación con contraseña maestra
while True:
    contraseña_maestra = getpass.getpass("Ingrese su contraseña maestra: ")
    clave_maestra = generar_clave_maestra(contraseña_maestra)

    # Verificar la contraseña maestra aquí
    # ...

    break  # Rompe el bucle si la autenticación es exitosa

# Menú principal
while True:
    print("\n1. Agregar Contraseña\n2. Obtener Contraseña\n3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_contraseña(clave_maestra)
    elif opcion == "2":
        obtener_contraseña(clave_maestra)
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Intente de nuevo.")
