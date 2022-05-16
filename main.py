# Nuestro __init__.py hace que el directorio website sea un paquete de python, lo que provoca que podamos
# importarlo en nuestro código además podremos traer la función que creó nuestra app ya lista ya que el archivo
# init ejecuta su contenido al ser importado.

from website import create_app

# Llamamos a la función para crear la app con sus configuraciones y la asigamos a una
# variable.
app = create_app()

# Solo se ejecutará nuestro servidor web si corremos este archivo main.py 
if __name__ == '__main__':
    app.run(debug=True)
