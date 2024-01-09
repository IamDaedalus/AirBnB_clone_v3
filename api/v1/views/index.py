#!/usr/bin/python3
"""the Flask app's index"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """returns the status on app_views"""
    status = { "status": "OK" }
    return jsonify(status)
