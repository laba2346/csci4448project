from .Animal import Animal
from .SpeciesInfo import SpeciesInfo

class Monkey(Animal):
    speciesInfo = SpeciesInfo("Monkey", "Cute and cuddly. Great at climbing trees and throwing poop", "Nuts and bananas", "Jungle", "Macaca Fascicularis")

    def __init__(self, name, sex, age, healthy, canClimbTrees):
        super().__init__(name, sex, age, healthy)
        self.canClimbTrees = canClimbTrees == "Yes"

    def getCanClimbTrees(self):
        return self.canClimbTrees

    def getCanClimbTreesEnglish(self):
        if(self.canClimbTrees):
            return "Yes"
        else:
            return "No"

    def setCanClimbTrees(self, canClimbTrees):
        self.canClimbTrees = canClimbTrees

    def getDetailedInfo(self):
        info = []
        info.append(("Name", self.name))
        info.append(("Sex", self.sex))
        info.append(("Age", self.age))
        info.append(("Healthy?", self.getHealthyEnglish()))
        info.append(("Species", self.getSpeciesInfo().getName()))
        info.append(("Old enough to climb trees safely?", self.getCanClimbTreesEnglish()))

        return info
        
    @staticmethod
    def getSpeciesInfo():
        return Monkey.speciesInfo
