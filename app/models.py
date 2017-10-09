"""Defines the Database Models of the application
Classes(Models):
  User: Represents a user in the database
  Role: Defines the role of a user in the application
"""

from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin

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
      role_id = db.Column(db.Intefer, db.ForeignKey('roles.id'))

class Role(db.Model):
      """"Creates the Roles defined for the users of the application
      Attributes:
        users(object): Represents the users associated with a certain role
      """
      pass
      