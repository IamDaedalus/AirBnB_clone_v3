#!/usr/bin/python3
"""the Flask app's index"""

from api.v1.views import app_views
import json

@app_views.route('/status')
def get_status(app_views):
    """returns the status on app_views"""
    my_json = { "status": 'OK' }
    return json.dumps(my_json)
