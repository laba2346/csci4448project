from ..models.Employee import *
from ..models.EmployeeFactory import *
from flask_login import current_user, login_user, login_required, logout_user
from flask import render_template, redirect, url_for, request

from app.forms import LoginForm


class UserController:
    def __init__(self):
        self.employeeFactory = EmployeeFactory()

    def findUser(self, desired_username):
        user_file = open("user_file.txt")
        for line in user_file:
            fields = line.split(',')
            userID = fields[0]
            firstName = fields[1]
            lastName = fields[2]
            email = fields[3]
            username = fields[4]
            password = fields[5]
            role = fields[6]
            preferredSpecies = fields[7]
            treatingAnimalID = int(fields[8])
            assignedEnclosureID = int(fields[9])
            if username == desired_username:
                return self.employeeFactory.getEmployee(firstName,lastName, email, username, password, userID, role, preferredSpecies, treatingAnimalID, assignedEnclosureID)
        return None

    def editUser(self):
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        userID = current_user.getNumericID()
        role = current_user.getRole()
        file = open('user_file.txt', 'r')
        userLines = file.readlines()
        file.close()

        file2 = open('user_file.txt', 'w')
        for line in userLines:
            fields = line.split(',')
            remainder = ','.join(fields[6:])
            if(int(line[0]) != int(userID)):
                file2.write(line)
            else:
                newLine = userID + ',' + firstName + ',' + lastName + ',' + email + ',' + username + ',' + password + ',' + remainder
                file2.write(newLine)
        file2.close()

        return redirect(url_for('settings'))

    def login(self):
        if(current_user.is_authenticated):
            return redirect(url_for('index'))
        form = LoginForm()
        if(form.validate_on_submit()):
            user = self.findUser(form.username.data)
            if user is None or not user.getCredentials().checkPassword(form.password.data):
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        return render_template('login.html', form=form)

    def logout(self):
        logout_user()
        return redirect(url_for('login'))
