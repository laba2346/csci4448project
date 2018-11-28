from ..models.Animal import *
from ..models.Zoo import *
from ..models.Employee import *
from ..models.Enclosure import *
from ..models.AnimalFactory import *
from ..models.SpeciesInfo import *
from flask import render_template, redirect, url_for, request
from flask_login import current_user
from app import zoo
import random
import json

class ZooController:
    def getZoo(self):
        return zoo

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
        newAnimal = AnimalFactory.getAnimal(name, sex, age, True, species, other)
        zoo.addAnimalToEnclosure(newAnimal, int(enclosureID))

        return redirect(url_for('animals'))

    def editAnimal(self):
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
        zoo.removeAnimalFromEnclosure(int(enclosureID), int(animalID))
        return redirect(url_for('animals'))

    def addEnclosure(self):
        zoo.addEnclosure(Enclosure([], "", ""))
        return redirect(url_for('enclosures'))

    def editEnclosure(self):
        foodType = request.form['foodType']
        cleanliness = request.form['cleanliness']
        enclosureID = int(request.form['enclosureID'])

        for enclosure in zoo.getEnclosures():
            if(enclosure.getID() == enclosureID):
                enclosure.setFoodType(foodType)
                enclosure.setCleanliness(cleanliness)

        return redirect(url_for('enclosures'))

    def deleteEnclosure(self, enclosureID):
        print(enclosureID)
        zoo.removeEnclosure(enclosureID)
        return redirect(url_for('enclosures'))


    def constructKeeperChart(self):
        data = {}
        datasets = []
        dataset = {}
        dataPoints = []
        labels = []
        colors = []
        for species in zoo.getSpeciesList():
            speciesName = species.getName()
            labels.append(speciesName)
            colors.append("#%06x" % random.randint(0, 0xFFFFFF))
            count = 0
            for enclosure in zoo.getEnclosures():
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
        for enclosure in zoo.getEnclosures():
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
