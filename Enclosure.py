from Animal import *


class Enclosure:
    id = 1

    def __init__(self, animals, foodType, cleanliness):
        self.animals = animals
        self.foodType = foodType
        self.cleanliness = cleanliness
        self.assignedKeeper = None
        self.id = Enclosure.id
        Enclosure.id += 1

    # Getters
    def getAnimals(self):
        return self.animals

    def getFoodType(self):
        return self.foodType

    def getCleanliness(self):
        return self.cleanliness

    def getAssignedKeeper(self):
        return self.assignedKeeper

    def getID(self):
        return self.id

    # Setters
    def setAnimals(self, animals):
        self.animals = animals

    def setFoodType(self, foodType):
        self.foodType = foodType

    def setCleanliness(self, cleanliness):
        self.cleanliness = cleanliness

    def setAssignedKeeper(self, assignedKeeper):
        self.assignedKeeper = assignedKeeper

    def addAnimal(self, animal):
        self.animals.append(animal)
