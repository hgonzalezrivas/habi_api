"""
Test houses services
"""
import json
import sys

sys.path.append('..')
from app import app as flask_app


def test_get_houses_success(mocker):
    """
    Test success response of get houses service
    """
    with flask_app.app_context():
        mocker.patch('database.Database.get_house_list', return_value=list())
        client = flask_app.test_client()
        response = client.get('/house?status=1&city=one_city&year=2015')
        assert response.status_code == 200


def test_get_houses_invalid_status():
    """
    Test get_houses service with invalid house status
    """
    with flask_app.app_context():
        client = flask_app.test_client()
        response = client.get('/house?status=100&city=one_city&year=2015')
        assert response.status_code == 400


def test_get_houses_internal_server_error(mocker):
    """
    Test get_houses service with internal server error
    """
    with flask_app.app_context():
        mocker.patch('database.Database.get_house_list', side_effect=ConnectionError('Error connecting to database'))
        client = flask_app.test_client()
        response = client.get('/house?status=1&city=one_city&year=2015')
        assert response.status_code == 500


def test_post_reaction_success(mocker):
    """
    Test success response of get houses service
    """
    with flask_app.app_context():
        mocker.patch('database.Database.insert_house_reaction', return_value=1)
        client = flask_app.test_client()
        response = client.post('/house/1/reaction', data=json.dumps({'idUser': 1}))
        assert response.status_code == 201


def test_post_reaction_bad_request():
    """
    Test bad request response of house reaction service
    """
    with flask_app.app_context():
        client = flask_app.test_client()
        response = client.post('/house/1/reaction', data=json.dumps({'id': 1}))
        assert response.status_code == 400


def test_post_reaction_internal_server_error(mocker):
    """
    Test success response of get houses service
    """
    with flask_app.app_context():
        mocker.patch('database.Database.insert_house_reaction', side_effect=ConnectionError('Table does not exists'))
        client = flask_app.test_client()
        response = client.post('/house/1/reaction', data=json.dumps({'idUser': 1}))
        assert response.status_code == 500