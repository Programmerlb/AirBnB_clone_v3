#!/usr/bin/python3
'''
    RESTful API actions for City objects
'''
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State
from models.place import Place
from models.city import City
from models.user import User


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_all_cities():
    '''
        Retrieve all city objects
    '''
    city_list = []
    for city in storage.all('City').values():
        state_list.append(city.to_dict())
    return jsonify(city_list)


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city(city_id):
    '''
        Retrieve one City object
    '''
    try:
        city = storage.get('City', city_id)
        return jsonify(city.to_dict())
    except Exception:
        abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city(city_id):
    '''
        Delete a City object
    '''
    try:
        city = storage.get('City', city_id)
        storate.delete(city)
        return jsonify({}), 200
    except Exception:
        abort(404)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def post_city(state_id):
    '''
        Create a State object
    '''
    if not request.json:
        return jsonify({"error": "Not a JSON"}), 400
    if 'name' not in request.json:
        return jsonify({"error": "Missing name"}), 400
    new_city = City(**request.get_json())
    new_city.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<string:city_id>', methods=['PUT'],
                 strict_slashes=False)
def put_city(city_id):
    '''
        Update a State object
    '''
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    if not request.json:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in request.getjson():
        if key not in ['id', 'created_at', 'state_id', 'updated_at']:
            setattr(city, attr, value)
    city.save()
    return jsonify(city.to_dict())
