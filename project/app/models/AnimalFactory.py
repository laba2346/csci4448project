from .Gorilla import Gorilla
from .Monkey import Monkey
from .PolarBear import PolarBear

class AnimalFactory:
    @staticmethod
    def getAnimal(name, sex, age, healthy, animalType, other):
        """Given a species name, create an animal of corresponding species

        Args:
            name (string): Animal name
            sex (string): Male or female
            age (int): Age of animal
            healthy (bool): Health status of animal
            animalType (string): Species name that dictates instantation
            other (Dictionary): Any unique parameters to the subclasses
        Returns:
            Animal: New animal of desired subclass

        """
        if(animalType == "Monkey"):
            return Monkey(name, sex, age, healthy, other['canClimbTrees'])
        elif(animalType == "Gorilla"):
            return Gorilla(name, sex, age, healthy, other['friendlyEnough'])
        elif(animalType == "Polar bear"):
            return PolarBear(name, sex, age, healthy, other['canReproduce'])

        return None
