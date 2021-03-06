from app import login
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user

from app import app
from app.forms import LoginForm
from app.models.Employee import Employee
from app.models.Animal import Animal
from app.models.Enclosure import Enclosure
from app.controllers.ZooController import *
from app.controllers.AnimalController import *
from app.controllers.EnclosureController import *
from app.controllers.EmployeeController import *


### Displaying Pages ###
@app.route('/')
@app.route('/index')
@login_required
def index():
    """Renders the homepage. Login required

    Args:
        None
    Returns:
        werkzeug.wrappers.Response: Flask response object for redirecting user.

    """
    if(current_user.getRole() == "Zookeeper"):
        data = zooController.constructKeeperChart()
        return render_template("index.html", current_user=current_user, enclosure=current_user.getAssignedEnclosure(), data=data)
    else:
        data = zooController.constructVetChart()
        return render_template("index.html", current_user=current_user, animal=current_user.getAnimalTreating(), data=data)

@app.route('/animals')
@login_required
def animals():
    """Renders the animals page. Login required

    Args:
        None
    Returns:
        werkzeug.wrappers.Response: Flask response object for redirecting user.

    """
    return render_template("animals.html", user=current_user, enclosures=zooController.getZoo().getEnclosures(), species=zooController.getZoo().getSpeciesList())

@app.route('/enclosures')
@login_required
def enclosures():
    """Renders the enclosures page. Login required

    Args:
        None
    Returns:
        werkzeug.wrappers.Response: Flask response object for redirecting user.

    """
    return render_template("enclosures.html", user=current_user, enclosures=zooController.getZoo().getEnclosures())

@app.route('/species')
@login_required
def species():
    """Renders the species page. Login required

    Args:
        None
    Returns:
        werkzeug.wrappers.Response: Flask response object for redirecting user.

    """
    return render_template("species.html", user=current_user, species=zooController.getZoo().getSpeciesList())

@app.route('/settings')
@login_required
def settings():
    """Renders the settings page. Login required

    Args:
        None
    Returns:
        werkzeug.wrappers.Response: Flask response object for redirecting user.

    """
    return render_template("settings.html", user=current_user)

@login.user_loader
def load_user(username):
    """Loads the user in order to maintain session/login. Uses flask_login

    Args:
        None
    Returns:
        werkzeug.wrappers.Response: Flask response object for redirecting user.

    """
    return employeeController.findEmployee(username)


zooController = ZooController()
employeeController = EmployeeController()
animalController = AnimalController()
enclosureController = EnclosureController()

### User interaction; uses controllers ###
app.add_url_rule('/login', 'login', employeeController .login, methods=["GET", "POST"])
app.add_url_rule('/logout', 'logout', employeeController .logout)
app.add_url_rule('/add-animal', 'addAnimal', animalController.addAnimal, methods=["POST"])
app.add_url_rule('/edit-animal', 'editAnimal', animalController.editAnimal, methods=["POST"])
app.add_url_rule('/delete-animal/<path:enclosureID>/<path:animalID>/', 'deleteAnimal', animalController.deleteAnimal)
app.add_url_rule('/create-new-enclosure', 'create-new-enclosure', enclosureController.addEnclosure)
app.add_url_rule('/edit-enclosure', 'editEnclosure',enclosureController.editEnclosure, methods=["POST"])
app.add_url_rule('/delete-enclosure/<path:enclosureID>', 'deleteEnclosure', enclosureController.deleteEnclosure)
app.add_url_rule('/edit-user', 'editUser', employeeController .editEmployee, methods=["POST"])
