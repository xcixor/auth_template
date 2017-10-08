"""Contains the configuration sets for the application"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Contains settings that are common to all configurations.
    Subclasses define settings specific for a configuration.
    Additional settings can be added to the class.
    Attributes:
        SECRET_KEY(string): Used by Flask-WTF extension to protect form data from Cross Site Forgery
            by generating encrypted tokens to verify the authenticity of request with form data.
        SQLALCHEMY_COMMIT_ON_TEARDOWN(boolean): When set True
            enables the automatic commit of sqlite database changes at the end of each request.
            FLASKY_MAIL_SUBJECT_PREFIX(String): Appended to email message
            to indicate some sort of title (subject to further research)
        FLASKY_MAIL_SENDER(String): The sender of the email
        FLASKY_ADMIN(String): The administrator of the app's database
    Methods:
        init_app(): Initializes configurations
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Your Cross Site Forgery Attempts are Futile'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[My_App]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <pndungu54@gmail.com.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        """Initializes configurations
        Args:
            app(object): an application object
        """
        pass

class DevelopmentConfig(Config):
    """Contains the configuration settings used when developing the app.
    Attributes:
        DEBUG (Boolean): An attribute that activates the debugger and the reloader.
        MAIL_SERVER (String): The application that receives incoming e-mail
        MAIL_PORT (String): The Port of the email server
        MAIL_USE_TLS (Boolean): Enables Transport Layer Security (TLS) security
        MAIL_USERNAME (String) Mail account username
        MAIL_PASSWORD (String) Mail account password
        SQLALCHEMY_DATABASE_URI (String): A URL that gives the location of the app's database
        Methods:
        _
    """
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    """Contains the configurations used during testing
    Attributes:
        TESTING (Boolean): An attribute that indicates test
        SQLALCHEMY_DATABASE_URI (String): A URL that gives the location of the app's database
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    """Contains the configurations for the publicly available app
    Attributes:
        SQLALCHEMY_DATABASE_URI (String): A URL that gives the location of the app's database
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    """A dictionary registering the different configurations"""
    
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

