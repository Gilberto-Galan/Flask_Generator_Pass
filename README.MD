
# Generador de Contraseñas
Este proyecto es una aplicación web sencilla desarrollada con Flask que permite generar contraseñas seguras con diversas opciones de personalización. Los usuarios pueden especificar la longitud de la contraseña, si desean incluir caracteres especiales o dígitos, y obtener una contraseña generada aleatoriamente.

Además, incluye una funcionalidad de copiar la contraseña al portapapeles para mejorar la experiencia del usuario.


## Tecnologias

- **Flask:** Framework de Python utilizado para el backend de la aplicación
- **Python:** Lenguaje de programación para la logica de la aplicación.
- **Bootstrap 5:** Framework CSS para diseñar la interfaz de usuario.
- **Jinja2:** Motor de plantillas integrado en Flask para la renderización dinamica de HTML.
- **JavaScript:** Para agregar la funcionalidad de copiar al portapapeles.
- **Librerias de Python:** `random` y `string` para generar contraseñas aleatorias


## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado Python 3 y pip en tu sistema.

### Instalación de depencias

Clona este repositorios
```bash
  git clone https://github.com/Gilberto-Galan/Flask_Generator_Pass.git
```

Navega al directorio del proyecto:

```bash
cd Flask-generator
```

Instala las dependencias necesarias:

```bash
pip install flask
```


### Ejecutar la aplicación

Ejecuta la aplicación Flask:
```bash
python app.py
```


Abre tu navegador web y accede a la siguiente URL:
```bash
http://127.0.0.1:5000/
```

### Funcionalidades

- **Generación de contraseñas:** El usuario puede generar una contraseña aleatoria con una longitud definida.
- **Personalización:** El usuario puede optar por incluir dígitos y caracteres especiales en la contraseña.
- **Copiar al portapapeles:** Una vez que la contraseña es generada, el usuario puede copiarla fácilmente al portapapeles utilizando un botón.

