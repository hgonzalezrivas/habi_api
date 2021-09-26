# HABI - API de Propiedades

## Introducción

- API generada con [Flask](https://flask.palletsprojects.com/en/2.0.x/)
+ [Python 3.8](https://www.python.org/downloads/release/python-389/).

- Despliegue de API con [gunicorn](https://gunicorn.org/)
y [Docker](https://www.docker.com/)

Para despliegue de proyecto se consideran 3 fases:

1. Desarrollo de API con Flask, conectada a base de datos
    con [PyMySQL](https://pymysql.readthedocs.io/en/latest/).
2. Despliegue de Microservicios en Docker con gunicorn.
3. Actualización de modelo de base de datos.


## Prerequisitos

- Instala [Python 3.8](https://www.python.org/downloads/release/python-389/)

- Instala y configura [Docker Desktop](https://docs.docker.com/desktop/#download-and-install).

Para pruebas locales, habilita el entorno virtual de 
Python e instala las librerías del proyecto.

```commandline
python -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
```

## Despliegue

Una vez configurado e instalado Docker, ejecuta lo siguiente
dentro del servidor donde será desplegado:


```commandline
docker-compose up
```

Esto genera la imagen de Docker y la inicializa, completando
así el despliegue del API, misma que se puede consultar en [este
archivo](https://github.com/hgonzalezrivas/habi_api/blob/master/openapi.yaml)


## Segunda Fase

Se propone un modelo de base de datos como el que se indica a
continuación:

![alt text](https://github.com/hgonzalezrivas/habi_api/blob/master/bd_hapi.png?raw=true)


- Se cuenta con un catálogo de ciudades y estados.
- Consulta de menor costo, ya que no hacemos un filtro de
estatus al último actualizado.
- Se incluye también el modelo para la tabla de reacciones de
usuario, con una relación entre la tabla de propiedades y la tabla
de usuarios.
