from app import login
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user

from app import app
from app import zooController, userController
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
    return render_template("index.html", current_user=current_user)

@app.route('/about')
@login_required
def about():
    return render_template("about.html")

@app.route('/animals')
@login_required
def animals():
    return render_template("animals.html", enclosures=zooController.getZoo().getEnclosures(), species=zooController.getZoo().getSpeciesList())

@app.route('/enclosures')
@login_required
def enclosures():
    return render_template("enclosures.html", enclosures=zooController.getZoo().getEnclosures())

@login.user_loader
def load_user(username):
    return userController.find_user(username)



### User interaction; uses controllers ###
app.add_url_rule('/login', 'login', userController.login, methods=["GET", "POST"])
app.add_url_rule('/logout', 'logout', userController.logout)
app.add_url_rule('/add-animal', 'addAnimal', zooController.addAnimal, methods=["POST"])
app.add_url_rule('/delete-animal/<path:enclosureID>/<path:animalID>/', 'deleteAnimal', zooController.deleteAnimal)
app.add_url_rule('/create-new-enclosure', 'create-new-enclosure', zooController.addEnclosure)
