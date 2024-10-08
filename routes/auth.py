from flask import Blueprint, render_template, request, redirect, url_for, flash
# from flask_jwt_extended import JWTManager
import requests
from flask_login import login_user, logout_user

from models.user import authenticate

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        domain = request.form['domain']
        user = authenticate(username, password, domain)
        if user:
            login_user(user)
            return render_template('login.html')

        else:
            flash('Не корректные данные для входа')
            return render_template('login.html')

@auth.route('/logout')
def logout():
    print('logout')
    logout_user()
    return render_template('index.html')
