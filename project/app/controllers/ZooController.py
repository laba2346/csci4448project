from ..models.Animal import *
from ..models.Zoo import *
from ..models.Employee import *
from ..models.Enclosure import *
from ..models.AnimalFactory import *
from ..models.SpeciesInfo import *
from ..models.EmployeeFactory import *
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from app.forms import LoginForm

import random
import json

class ZooController:
    def __init__(self):
        #test
        self.animalFactory = AnimalFactory()
        self.employeeFactory = EmployeeFactory()

        jimbo = AnimalFactory.getAnimal("Jimbo", "Male", 3, True, "Monkey", {'canClimbTrees':"Yes"})
        max = AnimalFactory.getAnimal("Max", "Male", 1.5, False, "Monkey", {'canClimbTrees':"No"})
        bob = AnimalFactory.getAnimal("Bob", "Male", 3, False, "Gorilla", {'friendlyEnough':"Yes"})
        pooh = AnimalFactory.getAnimal("Pooh", "Male", 1, True, "Polar bear", {'canReproduce':"Yes"})

        enclosure_1 = Enclosure([jimbo, max, bob], "Fruit & Nuts", "Clean")
        enclosure_2 = Enclosure([pooh], "Fish", "Clean")

        landon = self.employeeFactory.getEmployee("Landon", "Baxter", "landon.baxter@colorado.edu", "landon", "password",1,"Zookeeper","Monkey",1)
        landonvet = self.employeeFactory.getEmployee("Landon", "Baxter", "landon.baxter@colorado.edu", "landonvet", "password",2,"Veterinarian","",2)

        self.zoo = Zoo([enclosure_1, enclosure_2],[landon, landonvet])


    def getZoo(self):
        return self.zoo

    def addAnimal(self):
        name = request.form['name']
        species = request.form['species']
        age = request.form['age']
        sex = request.form['sex']
        enclosureID = request.form['enclosure']
        other = {}
        other['canClimbTrees'] = request.form['canClimbTrees']
        other['friendlyEnough'] = request.form['friendlyEnough']
        other['canReproduce'] = request.form['canReproduce']
        newAnimal = self.animalFactory.getAnimal(name, sex, age, True, species, other)
        self.zoo.addAnimalToEnclosure(newAnimal, int(enclosureID))

        return redirect(url_for('animals'))

    def editAnimal(self):
        name = request.form['name']
        sex = request.form['sex']
        age = request.form['age']
        healthy = (request.form['healthy'] == "Yes")
        animalID = int(request.form['animalID'])

        for enclosure in self.zoo.getEnclosures():
            for animal in enclosure.getAnimals():
                if(animal.getID() == animalID):
                    animal.setName(name)
                    animal.setSex(sex)
                    animal.setAge(age)
                    animal.setHealthy(healthy)

        return redirect(url_for('animals'))


    def deleteAnimal(self, enclosureID, animalID):
        self.zoo.removeAnimalFromEnclosure(int(enclosureID), int(animalID))
        return redirect(url_for('animals'))

    def addEnclosure(self):
        self.zoo.addEnclosure(Enclosure([], "", ""))
        return redirect(url_for('enclosures'))

    def editEnclosure(self):
        foodType = request.form['foodType']
        cleanliness = request.form['cleanliness']
        enclosureID = int(request.form['enclosureID'])

        for enclosure in self.zoo.getEnclosures():
            if(enclosure.getID() == enclosureID):
                enclosure.setFoodType(foodType)
                enclosure.setCleanliness(cleanliness)

        return redirect(url_for('enclosures'))

    def deleteEnclosure(self, enclosureID):
        print(enclosureID)
        self.zoo.removeEnclosure(enclosureID)
        return redirect(url_for('enclosures'))

    def findEmployee(self, desiredUsername):
        for user in self.zoo.getEmployees():
            if(user.getCredentials().getUsername() == desiredUsername):
                return user
        return None

    def editEmployee(self):
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if(password == ""):
            password = current_user.getCredentials().getPassword()
        userID = current_user.getNumericID()
        role = current_user.getRole()

        for user in self.zoo.getEmployees():
            if(user.getNumericID() == userID):
                user.getContactInfo().setFirstName(firstName)
                user.getContactInfo().setLastName(lastName)
                user.getContactInfo().setEmail(email)
                user.getCredentials().setUsername(username)
                user.getCredentials().setPassword(password)

        return redirect(url_for('settings'))

    def login(self):
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
        logout_user()
        return redirect(url_for('login'))

    def constructKeeperChart(self):
        data = {}
        datasets = []
        dataset = {}
        dataPoints = []
        labels = []
        colors = []
        for species in self.zoo.getSpeciesList():
            speciesName = species.getName()
            labels.append(speciesName)
            colors.append("#%06x" % random.randint(0, 0xFFFFFF))
            count = 0
            for enclosure in self.zoo.getEnclosures():
                for animal in enclosure.getAnimals():
                    if(animal.getSpeciesInfo().getName() == speciesName):
                        count += 1
            dataPoints.append(count)
        dataset['label'] = 'Animals'
        dataset['backgroundColor'] = colors
        dataset['data'] = dataPoints
        datasets.append(dataset)
        data['labels'] = labels
        data['datasets'] = datasets

        return data

    def constructVetChart(self):
        data = {}
        datasets = []
        dataset = {}
        dataPoints = [0,0]
        labels = ["Healthy","Unhealthy"]
        colors = ['#00ff00', '#ff0000']
        for enclosure in self.zoo.getEnclosures():
            for animal in enclosure.getAnimals():
                if(animal.getHealthy()):
                    dataPoints[0] += 1
                else:
                    dataPoints[1] += 1
        dataset['label'] = 'Animal health'
        dataset['backgroundColor'] = colors
        dataset['data'] = dataPoints
        datasets.append(dataset)
        data['labels'] = labels
        data['datasets'] = datasets

        return data
