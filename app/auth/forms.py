"""Defines the forms used for authentication
"""

from flask_wtf import Form

from wtforms import StringField, PasswordField, BooleanField, SubmitField

from wtforms.validators import Required, Email

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



