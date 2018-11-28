from .Employee import Employee

class Zookeeper(Employee):
    def __init__(self, contactInfo, credentials, id, preferredSpeciesName, assignedEnclosureID):
        super().__init__(contactInfo, credentials, id, "Zookeeper")
        self.preferredSpeciesName = preferredSpeciesName
        self.assignedEnclosureID = assignedEnclosureID

    def getPreferredSpeciesName(self):
        return self.preferredSpeciesName

    def getAssignmentID(self):
        return self.assignedEnclosureID

    def setPreferredSpeciesName(self, preferredSpeciesName):
        self.preferredSpecies = preferredSpeciesName

    def setAssignedEnclosureID(self, assignedEnclosureID):
        self.assignedEnclosureID = assignedEnclosureID
