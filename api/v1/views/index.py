#!/usr/bin/python3
"""the Flask app's index"""

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from api.v1.views import app_views
from models import storage
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """returns the status on app_views"""
    status = { "status": "OK" }
    # www.geeksforgeeks.org/how-to-return-a-json-response-from-a-flask-api/
    return jsonify(status)

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def obj_count():
    return jsonify(
            {
                "amenities": storage.count(Amenity),
                "cities": storage.count(City),
                "places": storage.count(Place),
                "reviews": storage.count(Review),
                "states": storage.count(State),
                "users": storage.count(User),
            }
            )
