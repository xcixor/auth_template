"""This module imports the auth blueprint.
It also defines the routes associated with user authenication.
"""
from flask import render_template, redirect, request, url_for, flash

from flask_login import login_user

from . import auth

from ..models import User

from .forms import LoginForm

from . import auth

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

