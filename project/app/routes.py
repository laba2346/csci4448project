from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user

from app import app
from app import zoo
from app.forms import LoginForm
from app.models.Employee import Employee
from app.models.Animal import Animal
from app.models.Enclosure import Enclosure
from app.controllers.UserController import *
from app.controllers.ZooController import *


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/animals')
def animals():
    return render_template("animals.html", enclosures=zoo.getEnclosures(), species=zoo.getSpeciesList())


@app.route('/enclosures')
def enclosures():
    return render_template("enclosures.html", enclosures=zoo.getEnclosures() )

@app.route('/delete-animal/<path:enclosureID>/<path:animalID>/')
def deleteAnimal(enclosureID, animalID):
    print(enclosureID, animalID)
    zoo.removeAnimalFromEnclosure(int(enclosureID), int(animalID))
    return redirect(url_for('animals'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if(current_user.is_authenticated):
        return redirect(url_for('index'))
    form = LoginForm()
    if(form.validate_on_submit()):
        user = find_user_username(form.username.data)
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/add-animal', methods=["POST"])
def addAnimal():
    name = request.form['name']
    species = zoo.getSpeciesObj(request.form['species'])
    age = request.form['age']
    sex = request.form['sex']
    enclosureID = request.form['enclosure']

    newAnimal = Animal(name, sex, species, age, True)
    zoo.addAnimalToEnclosure(newAnimal, int(enclosureID))
    return redirect(url_for('animals'))

@app.route('/create-new-enclosure')
def createEnclosure():
    zoo.addEnclosure(Enclosure([],"",""))
    return redirect(url_for('enclosures'))
