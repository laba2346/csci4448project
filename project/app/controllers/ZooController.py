from ..models.Animal import *
from ..models.Zoo import *
from ..models.Employee import *
from ..models.Enclosure import *
from ..models.AnimalFactory import *
from flask import render_template, redirect, url_for, request

class ZooController:
    def __init__(self):
        self.animalFactory = AnimalFactory

    def createZoo(self):
        species_list = ["Monkey", "Gorilla", "Polar bear"]

        jimbo = self.animalFactory.getAnimal("Jimbo", "M", 3, True, "Monkey")
        max = self.animalFactory.getAnimal("Max", "M", 1.5, True, "Monkey")
        bob = self.animalFactory.getAnimal("Bob", "M", 3, False, "Gorilla")
        pooh = self.animalFactory.getAnimal("Pooh", "M", 1, True, "Polar bear")

        enclosure_1 = Enclosure([jimbo, max, bob], "Fruit & Nuts", "Clean")
        enclosure_2 = Enclosure([pooh], "Fish", "Clean")

        self.zoo = Zoo([enclosure_1, enclosure_2],[], species_list)

    def getZoo(self):
        return self.zoo

    def addAnimal(self):
        name = request.form['name']
        species = request.form['species']
        age = request.form['age']
        sex = request.form['sex']
        enclosureID = request.form['enclosure']

        newAnimal = self.animalFactory.getAnimal(name, sex, age, True, species)
        self.zoo.addAnimalToEnclosure(newAnimal, int(enclosureID))

        return redirect(url_for('animals'))

    def deleteAnimal(self, enclosureID, animalID):
        self.zoo.removeAnimalFromEnclosure(int(enclosureID), int(animalID))

        return redirect(url_for('animals'))

    def addEnclosure(self):
        self.zoo.addEnclosure(Enclosure([], "", ""))

        return redirect(url_for('enclosures'))
