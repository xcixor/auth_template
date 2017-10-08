"""This is the app package constructor
It imports the flask extensions that are currently in use by the application.
It also imports other objects used by the application
It defines a method called 'create_app' which serves as the application factory.
This method takes as an argument, the name of the configuration to use for the app.
"""
from flask import Flask, render_template

from flask_bootstrap import Bootstrap

