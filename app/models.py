"""Defines the Database Models of the application
Classes(Models):
  User: Represents a user in the database
  Role: Defines the role of a user in the application
"""

from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from . import login_manager, db


class User(db.Model):
    """Instantiates a User object that can be stored in the db
    Attributes:
      __tablename__(string): Name of the table in the db
      id(Integer): A unique key that represents a particular user
      username(String): The username of the user
      role_id(Integer): Represents a foreign key to the Role table establishing one-many relationship
      email(String): Represents the user's email
    Methods:
      __repr__: Returns a string representation a string representation of the class
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

class Role(db.Model):
    """"Creates the Roles defined for the users of the application
    Attributes:
      id(Integer): A unique key that represents a particular role
      name(String): The name of the role
      users(object): Represents the users associated with a certain role
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

@login_manager.user_loader
def load_user(user_id):
    """loads a user with the given identifer for flask_login
    Args:
      user_id(integer): The id of the user to be loaded
    """
    return User.query.get(int(user_id))

# @app.route
# @login_required
# def secret():
#     """protects a route so that its only accessed by authenticated users"""
#     return "Unauthorized"
      