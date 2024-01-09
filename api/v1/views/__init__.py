#!/usr/bin/python3
"""index file for the Flask app"""

from flask import Blueprint
from api.v1.views import *

app_views = Blueprint('app_vies', __name__, url_prefix='/api/v1')
