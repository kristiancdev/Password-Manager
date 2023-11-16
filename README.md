# Gestor de Contraseñas en Python con Tkinter
Descripción
Este proyecto es un gestor de contraseñas implementado en Python, diseñado para proporcionar una solución segura para almacenar y gestionar contraseñas de manera local. La interfaz gráfica se implementa utilizando la biblioteca Tkinter, y las contraseñas se cifran antes de ser almacenadas.

> Estado de Desarrollo: En desarrollo

## Requisitos
- Python 3.x
- Biblioteca cryptography (instalable mediante pip install cryptography)

## Configuración del Entorno Virtual (Opcional)
Es recomendable utilizar un entorno virtual para aislar las dependencias del proyecto. A continuación, se proporcionan instrucciones para configurar y activar un entorno virtual:

```bash
# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual (en Windows)
venv\Scripts\activate

# Activar el entorno virtual (en macOS/Linux)
source venv/bin/activate
```

## Instalación de Dependencias
Instala las dependencias necesarias en el entorno virtual:

```bash
pip install -r requirements.txt
```

1. Se abrirá una ventana de login. Si es la primera vez que utilizas el gestor, ingresa y confirma tu nueva clave maestra. En caso contrario, ingresa tu clave maestra existente.
2. Una vez autenticado, podrás acceder al menú principal para agregar nuevas contraseñas o ver las contraseñas almacenadas.

## Desarrollo

Este proyecto está en una fase de desarrollo activa. Si deseas contribuir o realizar mejoras, sigue estos pasos:

  1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/gestor-contraseñas.git
cd gestor-contraseñas
```
  2. Crea y activa un entorno virtual.
  3. Instala las dependencias de desarrollo:
```bash
pip install -r requirements-dev.txt
```
  4. Realiza tus contribuciones y envía pull requests.

## Características Actuales
- **Agregar Contraseña:** Permite ingresar los detalles del sitio, usuario y contraseña para almacenarlos de forma segura.
- **Ver Contraseñas:** Visualiza las contraseñas almacenadas de forma segura. (En proceso)

## Consideraciones de Seguridad
- **Clave Maestra:** Asegúrate de recordar tu clave maestra. No hay forma de recuperar las contraseñas si olvidas la clave maestra.
- **Seguridad del Archivo:** Mantén seguro el archivo contraseñas.json. No lo compartas ni lo hagas público, ya que contiene información sensible.

