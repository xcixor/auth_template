"""This is the app package constructor
It imports the flask extensions that are currently in use by the application.
It also imports other objects used by the application
It defines a method called 'create_app' which serves as the application factory.
This method takes as an argument, the name of the configuration to use for the app.
"""
from flask import Flask

from flask_bootstrap import Bootstrap

from flask_mail import Mail

from flask_moment import Moment

from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

from config import config

# from .main import main as main_blueprint

#Creating the extensions objects

bootstrap = Bootstrap()

mail = Mail()

moment = Moment()

db = SQLAlchemy()


login_manager = LoginManager()

login_manager.session_protection = 'strong'

login_manager.login_view = 'auth.login'


#spacing in this method might cause problems, watchout for that

def create_app(config_name):
    """Initializes the app
    Args:
    config_name: The configuration to use for the app
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #Extensions
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    #BluePrints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    #routes and custom errors go here

    return app





