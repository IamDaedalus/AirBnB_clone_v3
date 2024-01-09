#!/usr/bin/python3
"""the Flask app's index"""

from api.v1.views import app_views
import json

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """returns the status on app_views"""
    status = { "status": 'OK' }
    return json.dumps(status)
