"""
Clase para implementación de llamadas a base de datos
"""
import pymysql
import config


class Database:

    def get_house_list(self) -> list:
        """Ejecuta query para obtener listado de casas

        :return: Listado de casas
        :rtype: list
        :raises:
            ConnectionError: Si existe algún error en la conexión
            o interacción con la base de datos
        """
        connection = None
        query = """
            SELECT a.id, a.address, a.city, a.price, a.description, a.year, \
                    s.label as status, s.id AS status_id \
            FROM property a \
            INNER JOIN \
                (SELECT MAX(id) as id, property_id, status_id \
                FROM status_history GROUP BY property_id) AS sh \
                ON sh.property_id = a.id \
            INNER JOIN status s \
                ON sh.status_id = s.id \
            ORDER BY a.id;
            """
        try:
            connection = pymysql.connect(
                host=config.DB_HOST,
                port=config.DB_PORT,
                user=config.DB_USER,
                passwd=config.DB_PASSWORD,
                db=config.DB_DATABASE
            )
            cur = connection.cursor()
            cur.execute(query)
            columns = [field[0] for field in cur.description]
            rows = cur.fetchall()
            response = [dict(zip(columns, row)) for row in rows]
            return response
        except Exception as exec:
            raise ConnectionError(str(exec)) from exec
        finally:
            if connection:
                connection.close()

    def insert_house_reaction(self, house_id: int, user_id: int) -> int:
        """Inserta una reacción de propiedad en la tabla ta_house_reaction

        :param house_id (int): Id de propiedad
        :param user_id (int): Id de usuario que inserta la reacción
        :return: Id almacenado en base de datos
        :rtype: int
        :raises:
            ConnectionError: Si existe algún error en la conexión
             o interacción con la base de datos
        """
        try:
            connection = pymysql.connect(
                host=config.DB_HOST,
                port=config.DB_PORT,
                user=config.DB_USER,
                passwd=config.DB_PASSWORD,
                db=config.DB_DATABASE
            )
            cur = connection.cursor()
            query = """
                INSERT INTO `ta_house_reaction` \
                  (`user_id`, `house_id`) \
                  VALUES (%s, %s);
            """
            cur.execute(query, (user_id, house_id))
            connection.commit()
            insert_id = cur.lastrowid
            return insert_id
        except Exception as ex:
            raise ConnectionError(str(ex)) from ex
        finally:
            if connection:
                connection.close()