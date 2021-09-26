"""
[HABI API]
"""
from flask import Flask, Response, request
from service import House

import exceptions

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def health_check():
    """
    Valida que el API esté trabajando correctamente, regresando la versión
    """
    return Response('[HABI] Version: ' + app.config['VERSION'],
                    status=200,
                    content_type='application/json')


@app.route('/house', methods=['GET'])
def get_houses():
    """
    Servicio de consulta.
    Obtiene el listado de propiedades
    """
    response = House(request).get_houses()
    return Response(response,
                    status=200,
                    content_type='application/json')


@app.route('/house/<id>/reaction', methods=['POST'])
def house_reaction(id):
    """
    Servicio "Me Gusta".
    Los usuarios podrán reaccionar a cada propiedad, y el registro queda
    almacenado en base de datos
    """
    House(request).insert_reaction()
    return Response('Success.',
                    status=201,
                    content_type='application/json')


app.register_error_handler(ValueError,
                           exceptions.handle_value_error)
app.register_error_handler(KeyError,
                           exceptions.handle_request_validation)
app.register_error_handler(AttributeError,
                           exceptions.handle_request_validation)
app.register_error_handler(ConnectionError,
                           exceptions.handle_internal_error)

if __name__ == '__main__':
    app.run()
