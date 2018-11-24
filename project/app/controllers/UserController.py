from ..models.Employee import *
from flask_login import current_user, login_user, login_required, logout_user
from flask import render_template, redirect, url_for, request

from app.forms import LoginForm


class UserController:
    def find_user(self, user_id):
        user_file = open("user_file.txt", 'r')
        for line in user_file:
            fields = line.split(',')
            line_user_id = fields[0]
            name = fields[1]
            username = fields[2]
            password = fields[3]
            print(line_user_id)
            if user_id == line_user_id:
                return Employee(name, username, password, str(user_id))
        return None

    def find_user_username(self, desired_username):
        user_file = open("user_file.txt")
        for line in user_file:
            fields = line.split(',')
            user_id = fields[0]
            name = fields[1]
            username = fields[2]
            password = fields[3]
            print(password)
            if username == desired_username:
                return Employee(name, username, password, str(user_id))
        return None

    def login(self):
        if(current_user.is_authenticated):
            return redirect(url_for('index'))
        form = LoginForm()
        if(form.validate_on_submit()):
            user = self.find_user_username(form.username.data)
            if user is None or not user.check_password(form.password.data):
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        return render_template('login.html', form=form)

    def logout(self):
        logout_user()
        return redirect(url_for('login'))
