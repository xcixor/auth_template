"""This module imports the auth blueprint.
It also defines the routes associated with user authenication.
"""
from flask import render_template, redirect, request, url_for, flash

from flask_login import login_user, logout_user, login_required, current_user

from . import auth

from ..models import User

from .forms import LoginForm, RegistrationForm

from . import auth

from .. import db

from ..emails import send_email

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    """Validates the User details and tries to Log the user in"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('/main.index'))
        flash('invalid username or password')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    """Removes and resets the user session"""
    logout_user()
    flash('You have logged out')
    redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


