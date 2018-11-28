from app import login
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user

from app import app
from app.forms import LoginForm
from app.models.Employee import Employee
from app.models.Animal import Animal
from app.models.Enclosure import Enclosure
from app.controllers.UserController import *
from app.controllers.ZooController import *


### Displaying Pages ###
@app.route('/')
@app.route('/index')
@login_required
def index():
    if(current_user.getRole() == "Zookeeper"):
        data = zooController.constructKeeperChart()
        return render_template("index.html", current_user=current_user, enclosure=zooController.getZoo().getEnclosureByID(current_user.getAssignmentID()), data=data)
    else:
        data = zooController.constructVetChart()
        return render_template("index.html", current_user=current_user, animal=zooController.getZoo().getAnimalByID(current_user.getAssignmentID()), data=data)

@app.route('/animals')
@login_required
def animals():
    return render_template("animals.html", user=current_user, enclosures=zooController.getZoo().getEnclosures(), species=zooController.getZoo().getSpeciesList())

@app.route('/enclosures')
@login_required
def enclosures():
    return render_template("enclosures.html", user=current_user, enclosures=zooController.getZoo().getEnclosures())

@app.route('/species')
@login_required
def species():
    return render_template("species.html", user=current_user, species=zooController.getZoo().getSpeciesList())

@app.route('/settings')
@login_required
def settings():
    return render_template("settings.html", user=current_user)

@login.user_loader
def load_user(username):
    return userController.findUser(username)


zooController = ZooController()
userController = UserController()

### User interaction; uses controllers ###
app.add_url_rule('/login', 'login', userController.login, methods=["GET", "POST"])
app.add_url_rule('/logout', 'logout', userController.logout)
app.add_url_rule('/add-animal', 'addAnimal', zooController.addAnimal, methods=["POST"])
app.add_url_rule('/edit-animal', 'editAnimal', zooController.editAnimal, methods=["POST"])
app.add_url_rule('/delete-animal/<path:enclosureID>/<path:animalID>/', 'deleteAnimal', zooController.deleteAnimal)
app.add_url_rule('/create-new-enclosure', 'create-new-enclosure', zooController.addEnclosure)
app.add_url_rule('/edit-enclosure', 'editEnclosure', zooController.editEnclosure, methods=["POST"])
app.add_url_rule('/delete-enclosure/<path:enclosureID>', 'deleteEnclosure', zooController.deleteEnclosure)
app.add_url_rule('/edit-user', 'editUser', userController.editUser, methods=["POST"])
