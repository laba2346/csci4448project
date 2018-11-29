from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from app.forms import LoginForm
from ..models.AnimalFactory import *
from app import zoo

class AnimalController:
    def addAnimal(self):
        """Adds an Animal to the zoo and redirects user accordingly

        Args:
            None. Flask request is implicitly passed, however.
        Returns:
            werkzeug.wrappers.Response: Flask response object for redirecting user.

        """
        name = request.form['name']
        species = request.form['species']
        age = request.form['age']
        sex = request.form['sex']
        enclosureID = request.form['enclosure']
        other = {}
        other['canClimbTrees'] = request.form['canClimbTrees']
        other['friendlyEnough'] = request.form['friendlyEnough']
        other['canReproduce'] = request.form['canReproduce']
        newAnimal = AnimalFactory.getAnimal(name, sex, age, True, species, other)
        zoo.addAnimalToEnclosure(newAnimal, int(enclosureID))

        return redirect(url_for('animals'))

    def editAnimal(self):
        """Edits an existing animal's information and redirects the user accordingly

        Args:
            None. Flask request is implicitly passed, however.
        Returns:
            werkzeug.wrappers.Response: Flask response object for redirecting user.

        """
        name = request.form['name']
        sex = request.form['sex']
        age = request.form['age']
        healthy = (request.form['healthy'] == "Yes")
        animalID = int(request.form['animalID'])

        for enclosure in zoo.getEnclosures():
            for animal in enclosure.getAnimals():
                if(animal.getID() == animalID):
                    animal.setName(name)
                    animal.setSex(sex)
                    animal.setAge(age)
                    animal.setHealthy(healthy)

        return redirect(url_for('animals'))


    def deleteAnimal(self, enclosureID, animalID):
        """Adds an Animal to the zoo and redirects user accordingly

        Args:
            enclosureID (int): ID corresponding to the animal's enclosure \n
            animalID (int): ID corresponding to the animal that needs to be deleted\n
        Returns:
            werkzeug.wrappers.Response: Flask response object for redirecting user.

        """
        zoo.removeAnimalFromEnclosure(int(enclosureID), int(animalID))
        return redirect(url_for('animals'))
