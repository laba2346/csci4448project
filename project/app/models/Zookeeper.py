from .Employee import Employee

class Zookeeper(Employee):
    def __init__(self, firstName, lastName, email, username, password, preferredSpecies, assignedEnclosure):
        super().__init__(firstName, lastName, email, username, password, "Zookeeper")
        self.preferredSpecies = preferredSpecies
        self.assignedEnclosure = assignedEnclosure


    def getPreferredSpecies(self):
        return self.preferredSpecies

    def getAssignedEnclosure(self):
        return self.assignedEnclosure

    def getAssignmentID(self):
        if(self.assignedEnclosure is not None):
            return self.assignedEnclosure.getID()
        return -1

    def setPreferredSpecies(self, preferredSpecies):
        self.preferredSpecies = preferredSpecies

    def setAssignedEnclosure(self, assignedEnclosure):
        self.assignedEnclosure = assignedEnclosure

    def removeAssignment(self):
        self.assignedEnclosure = None
