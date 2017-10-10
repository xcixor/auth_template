"""Contains the functionality for the home page"""
from flask import render_template

from . import main

@main.route('/')
def index():
    """Defines the home page"""
    return render_template('index.html')