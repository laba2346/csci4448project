from .Employee import Employee

class Zookeeper(Employee):
    def __init__(self, name, username, password, id, preferredSpecies):
        super().__init__(name, username, password, id, "Zookeeper")
        self.preferredSpecies = preferredSpecies

    def getPreferredSpecies(self):
        return self.preferredSpecies

    def setPreferredSpecies(self, preferredSpecies):
        self.preferredSpecies = preferredSpecies
