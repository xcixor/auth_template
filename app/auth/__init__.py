"""This is the auth blueprint constructor.
It creates the blueprint object and imports routes from views.py module.
"""
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views





