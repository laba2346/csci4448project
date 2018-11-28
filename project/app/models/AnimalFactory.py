from .Gorilla import Gorilla
from .Monkey import Monkey
from .PolarBear import PolarBear

class AnimalFactory:
    @staticmethod
    def getAnimal(name, sex, age, healthy, animalType, other):
        if(animalType == "Monkey"):
            return Monkey(name, sex, age, healthy, other['canClimbTrees'])
        elif(animalType == "Gorilla"):
            return Gorilla(name, sex, age, healthy, other['friendlyEnough'])
        elif(animalType == "Polar bear"):
            return PolarBear(name, sex, age, healthy, other['canReproduce'])

        return None
