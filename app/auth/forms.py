"""Defines the forms used for authentication
"""

from flask_wtf import Form

from wtforms import StringField, PasswordField, BooleanField, SubmitField

from wtforms.validators import Required, Email, Length, Email, Regexp, EqualTo

from wtforms import ValidationError

from ..models import User

class LoginForm(Form):
    """The login form that is presented to the user
    Attributes:
        email(String): user's email
        password(String): user's password
        remember_me(Boolean): indicates whether to repeat the login procedure the next time
        submit(Button): submits the user login details to the app
    Methods:

    """
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegistrationForm(Form):
    """The form presented to the user for registering an account
    Attributes:
        email(String): user's email
        password(String): user's password
        password2(String): confirmation of the previously input password
        submit(Button): submits the user login details to the app
    Methods:
        validate_email: ensures there is no duplicate email in the dbase
        validate_username: ensures there is no duplicate username in the dbase
    """
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    #The username uses regular expressions to ensure it contains letters, numbers, underscores, and dots only.
    username = StringField('Username', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')







