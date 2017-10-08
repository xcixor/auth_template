"""This module imports the auth blueprint.
It also defines the routes associated with user authenication.
"""
from flask import render_template

from . import auth

@auth.route('/login')
def login():
    """Logs the user in"""
    return render_template('auth/login.html')