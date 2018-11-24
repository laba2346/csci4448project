from .Gorilla import Gorilla
from .Monkey import Monkey
from .PolarBear import PolarBear

class AnimalFactory:
    def getAnimal(self, name, sex, age, healthy, animalType):
        if(animalType == "Monkey"):
            return Monkey(name, sex, age, healthy)
        elif(animalType == "Gorilla"):
            return Gorilla(name, sex, age, healthy)
        elif(animalType == "Polar bear"):
            return PolarBear(name, sex, age, healthy)

        return None
