from .AnimalFactory import AnimalFactory
from .Enclosure import Enclosure
from .Monkey import Monkey
from .Gorilla import Gorilla
from .PolarBear import PolarBear

class Zoo:
    def __init__(self, enclosures, employees):
        self.enclosures = enclosures
        self.employees = employees
        self.speciesList = [Monkey.getSpeciesInfo(), Gorilla.getSpeciesInfo(), PolarBear.getSpeciesInfo()]

    def addEnclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def removeEnclosure(self, enclosureID):
        self.enclosures = [enclosure for enclosure in self.enclosures if int(enclosure.getID()) != int(enclosureID)]

    def getEnclosures(self):
        return self.enclosures

    def getEnclosureByID(self, desiredID):
        for enclosure in self.enclosures:
            print(desiredID, enclosure.getID())
            if(enclosure.getID() == desiredID):
                return enclosure
        return None

    def addAnimalToEnclosure(self, animal, enclosureID):
        for e in self.enclosures:
            if(enclosureID == e.getID()):
                e.addAnimal(animal)

    def removeAnimalFromEnclosure(self, enclosureID, animalID):
        for i in range(0, len(self.enclosures)):
            if(self.enclosures[i].getID() == enclosureID):
                self.enclosures[i].removeAnimal(animalID)


    def getAnimalByID(self, desiredID):
        for enclosure in self.enclosures:
            animals = enclosure.getAnimals()
            for animal in animals:
                if(int(animal.getID()) == int(desiredID)):
                    return animal
        return None

    def getSpeciesList(self):
        return self.speciesList

    def getEmployees(self):
        return self.employees

    def setEmployees(self, employees):
        self.employees = employees
