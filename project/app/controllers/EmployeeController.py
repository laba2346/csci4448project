from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from app.forms import LoginForm
from app import zoo

class EmployeeController:
    def findEmployee(self, desiredUsername):
        """Finds an employee by username and returns the employee object. Used by flask-login to maintain a session

        Args:
            desiredUsername (string): Username of the desired user
        Returns:
            Employee: The object corresponding to the desired user. 'None' if not found.

        """
        for user in zoo.getEmployees():
            if(user.getCredentials().getUsername() == desiredUsername):
                return user
        return None

    def editEmployee(self):
        """Finds an employee by username and returns the employee object. Used by flask-login to maintain a session

        Args:
            None. Flask request object is implicitly passed and accessed, however
        Returns:
            werkzeug.wrappers.Response: Flask response object for redirecting user.

        """
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if(password == ""):
            password = current_user.getCredentials().getPassword()
        userID = current_user.getNumericID()
        role = current_user.getRole()

        for user in zoo.getEmployees():
            if(user.getNumericID() == userID):
                user.getContactInfo().setFirstName(firstName)
                user.getContactInfo().setLastName(lastName)
                user.getContactInfo().setEmail(email)
                user.getCredentials().setUsername(username)
                user.getCredentials().setPassword(password)

        return redirect(url_for('settings'))

    def login(self):
        """Creates the login form, authenticates the user, and redirects user if already logged in.

        Args:
            none
        Returns:
            werkzeug.wrappers.Response: Flask response object for redirecting user.

        """
        if(current_user.is_authenticated):
            return redirect(url_for('index'))
        form = LoginForm()
        if(form.validate_on_submit()):
            user = self.findEmployee(form.username.data)
            if user is None or not user.getCredentials().checkPassword(form.password.data):
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        return render_template('login.html', form=form)

    def logout(self):
        """Simply invokes the logout_user function from flask_login. Ends the user's session

        Args:
            none
        Returns:
            werkzeug.wrappers.Response: Flask response object for redirecting user.
        """
        logout_user()
        return redirect(url_for('login'))
