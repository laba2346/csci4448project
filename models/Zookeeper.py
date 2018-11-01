class Zookeeper(Employee):
    def __init__(self, preferredSpecies):
        Employee.__init__(self)
        self.preferredSpecies = preferredSpecies

    def getPreferredSpecies(self):
        return self.preferredSpecies

    def setPreferredSpecies(self, preferredSpecies):
        self.preferredSpecies = preferredSpecies
