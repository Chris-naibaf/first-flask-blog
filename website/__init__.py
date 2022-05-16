# Este archivo servirá para crear mi instancia de Flask, la instancia de Flask será la aplicación de mi sitio web
# que se encargará de las interacciónes entre el frontend, backend y bases de datos.

from flask import Flask

# Fabrica para la creación de mi app y sus configuraciones
def create_app():
    # Crea una instancia de flask y se le asigna el nombre del archivo en el que se
    # creó.
    app = Flask(__name__)

    # Llave que servirá para encriptar las cookies y datos de sesión.
    app.config['SECRET_KEY'] = 'dev'

    # Se devuelve la app ya inicializada y configurada
    return app  