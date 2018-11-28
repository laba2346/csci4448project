from .Animal import Animal
from .SpeciesInfo import SpeciesInfo

class Gorilla(Animal):
    speciesInfo = SpeciesInfo("Gorilla","Close relatives of the human, but much more dangerous.","Berries and nuts","Jungle","Troglodytes Gorilla")

    def __init__(self, name, sex, age, healthy, friendlyEnough):
        super().__init__(name, sex, age, healthy)
        self.friendlyEnough = friendlyEnough == "Yes" # Friendly enough for small enclosures w/ others

    def getFriendlyEnough(self):
        return self.friendlyEnough

    def getFriendlyEnoughEnglish(self):
        if(self.friendlyEnough):
            return "Yes"
        else:
            return "No"

    def setFriendlyEnough(self, friendlyEnough):
        self.friendlyEnough = friendlyEnough

    def getDetailedInfo(self):
        info = []
        info.append(("Name", self.name))
        info.append(("Sex", self.sex))
        info.append(("Age", self.age))
        info.append(("Healthy?", self.getHealthyEnglish()))
        info.append(("Species", self.getSpeciesInfo().getName()))
        info.append(("Friendly with other animals?", self.getFriendlyEnoughEnglish()))

        return info

    @staticmethod
    def getSpeciesInfo():
        return Gorilla.speciesInfo
