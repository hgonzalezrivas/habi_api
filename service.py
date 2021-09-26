"""
Paquete que incluye las clases de consumo de microservicios
"""
from constants import STATUS_LIST
from database import Database
import json
from model import Response, UserRequest


class House:

    def __init__(self, request):
        self.request = request

    def get_houses(self) -> Response:
        """Obtiene el listado de propiedades, a partir de la consulta de
        base de datos

        :return: Listado de propiedades
        :rtype: model.Response
        """

        # Inicializa objeto de clase Database, para consultas a base de datos
        db = Database()

        # Configura variables de microservicio
        house_status = self.request.args.get('status')
        house_city = self.request.args.get('city')
        house_year = self.request.args.get('year')

        # Validación de variables
        if house_status and not int(house_status) in STATUS_LIST:
            raise ValueError('Id of status out of range')

        # Consulta a base de datos
        response = db.get_house_list()

        # Implementa el filtro de búsqueda
        if house_status:
            response = list(filter(lambda x:
                                   (x['status_id'] == int(house_status)),
                                   response))

        if house_city:
            response = list(filter(lambda x:
                                   (x['city'] == house_city.lower()),
                                   response))

        if house_year:
            response = list(filter(lambda x:
                                   (x['year'] == int(house_year)),
                                   response))

        return Response(
            'Success.',
            response,
            len(response)
        ).to_json()

    def insert_reaction(self):
        """Inserta una reacción (Like) a la propiedad
        """

        # Inicializa objeto de clase Database, para consultas a base de datos
        db = Database()

        # Configura variables de microservicio
        house_id = self.request.view_args['id']
        user_id = UserRequest.from_dict(json.loads(self.request.data))

        db.insert_house_reaction(house_id, user_id)