"""serves as the entry point for the main module"""

from flask import Blueprint

main = Blueprint('main', __name__)

from . import errors, forms, views