from .Animal import Animal
from .SpeciesInfo import SpeciesInfo

class PolarBear(Animal):
    speciesInfo = SpeciesInfo("Polar bear", "Majestic, strong, but endangered.","Fish", "Polar", "Ursus maritimus")

    def __init__(self, name, sex, age, healthy, canReproduce):
        super().__init__(name, sex, age, healthy)
        self.canReproduce = canReproduce == "Yes"

    def getCanReproduce(self):
        return self.canReproduce

    def getCanReproduceEnglish(self):
        if(self.canReproduce):
            return "Yes"
        else:
            return "No"

    def setCanReproduce(self, canReproduce):
        self.canReproduce = canReproduce


    def getDetailedInfo(self):
        info = []
        info.append(("Name", self.name))
        info.append(("Sex", self.sex))
        info.append(("Age", self.age))
        info.append(("Healthy?", self.getHealthyEnglish()))
        info.append(("Species", self.getSpeciesInfo().getName()))
        info.append(("Suitable for mating?", self.getCanReproduceEnglish()))

        return info

    @staticmethod
    def getSpeciesInfo():
        return PolarBear.speciesInfo
