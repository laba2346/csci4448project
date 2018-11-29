from .AnimalFactory import AnimalFactory
from .Enclosure import Enclosure
from .Monkey import Monkey
from .Gorilla import Gorilla
from .PolarBear import PolarBear

class Zoo:
    def __init__(self, enclosures, employees):
        self.enclosures = enclosures
        print(self.enclosures[0])
        self.employees = employees
        self.speciesList = [Monkey.getSpeciesInfo(), Gorilla.getSpeciesInfo(), PolarBear.getSpeciesInfo()]

    def addEnclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def removeEnclosure(self, enclosureID):
        index = -1
        for i,enclosure in enumerate(self.enclosures):
            if int(enclosure.getID()) == int(enclosureID):
                index = i
        if(index != -1):
            for employee in self.employees:
                if(employee.getRole() == "Zookeeper"):
                    if(int(employee.getAssignmentID()) == int(enclosureID)):
                        employee.removeAssignment()
            del self.enclosures[index]


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
        animalID = int(animalID)
        enclosureID = int(enclosureID)
        for i in range(0, len(self.enclosures)):
            if(self.enclosures[i].getID() == enclosureID):
                self.enclosures[i].removeAnimal(animalID)

        for employee in self.employees:
            if(employee.getRole() == "Veterinarian" and employee.getAssignmentID() == animalID):
                employee.removeAssignment()

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
