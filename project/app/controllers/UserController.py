from ..models.Employee import *
from ..models.EmployeeFactory import *
from flask_login import current_user, login_user, login_required, logout_user
from flask import render_template, redirect, url_for, request

from app.forms import LoginForm


class UserController:
    def __init__(self):
        self.employeeFactory = EmployeeFactory()

    def find_user(self, desired_username):
        user_file = open("user_file.txt")
        for line in user_file:
            fields = line.split(',')
            user_id = fields[0]
            role = fields[1]
            name = fields[2]
            username = fields[3]
            password = fields[4]
            preferredSpecies = fields[5]
            treatingAnimalID = fields[6]
            print(desired_username)
            if username == desired_username:
                return self.employeeFactory.getEmployee(name, username, password, user_id, role, preferredSpecies, treatingAnimalID)
        return None

    def login(self):
        if(current_user.is_authenticated):
            return redirect(url_for('index'))
        form = LoginForm()
        if(form.validate_on_submit()):
            user = self.find_user(form.username.data)
            if user is None or not user.check_password(form.password.data):
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        return render_template('login.html', form=form)

    def logout(self):
        logout_user()
        return redirect(url_for('login'))
