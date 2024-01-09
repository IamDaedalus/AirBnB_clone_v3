#!/usr/bin/python3
"""basic Flask app setup"""

from os import environ
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown():
    """method that handles teardown appcontext"""
    storage.close()


if __name__ == "__main__":
    host = environ.get("HBNB_API_HOST") or "0.0.0.0"
    port = environ.get("HBNB_API_PORT") or 5000
    app.run(host=host, port=port, threaded=True)
