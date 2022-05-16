# Este archivo sirve para contener mis rutas que serán las vitas en el frontend.

# Gracias a este import podemos separar nuestras rutas y demás de nuestra aplicación
# para poder acceder a ellas en un archivo diferente y tener todo mas organizado.
from flask import Blueprint, render_template

views = Blueprint('views', __name__)


# Ejecuta la función home al acceder a la ruta '/'
@views.route('/')
def home():
    return render_template("home.html")