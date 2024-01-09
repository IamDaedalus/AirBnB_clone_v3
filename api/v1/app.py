#!/usr/bin/python3
"""basic Flask app setup"""

from os import getenv
from flask import Flask
from flask import jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception=None):
    """method that handles teardown appcontext"""
    storage.close()


@app.errorhandler(404)
def not_found_handler(e):
    """ 404 page handler """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
