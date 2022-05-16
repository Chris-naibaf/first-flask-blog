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

    # Importo mis blueprints con mis rutas e información relacionada a mi app.
    from .views import views
    from .auth import auth

    # Registro de la rutas en la app
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Se devuelve la app ya inicializada y configurada
    return app  