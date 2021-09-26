"""
Paquete de excepciones
"""
from model import Error


def handle_value_error(exception):
    """Error en parámetros

    :param exception: Excepcion generada
    :return: Objeto de respuesta con error
    """
    response = Error('Bad request.', str(exception))
    return response.to_json(), 400


def handle_request_validation(exception):
    """Error en petición

    :param exception: Excepcion generada
    :return: Objeto de respuesta con error
    """
    response = Error('Bad request.', str(exception))
    return response.to_json(), 400


def handle_internal_error(exception):
    """Error interno de servicio

    :param exception: Excepcion generada
    :return: Objeto de respuesta con error
    """
    response = Error('Internal server error.', str(exception))
    return response.to_json(), 500