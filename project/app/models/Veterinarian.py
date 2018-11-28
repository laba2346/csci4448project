from .Employee import Employee

class Veterinarian(Employee):
    def __init__(self, contactInfo, credentials, id, treatingAnimalID):
        super().__init__(contactInfo, credentials, id, "Veterinarian")
        self.treatingAnimalID = treatingAnimalID
        self.isTreatingAnimal = treatingAnimalID != -1

    def getIsTreatingAnimal(self):
        return self.isTreatingAnimal

    def getIsTreatingAnimalEnglish(self):
        return "Yes" if self.isTreatingAnimal else "No"

    def getAssignmentID(self):
        return self.treatingAnimalID

    def setTreatingAnimalID(self, treatingAnimalID):
        self.treatingAnimalID = treatingAnimalID

    def setIsTreatingAnimal(self, isTreatingAnimal):
        self.isTreatingAnimal = isTreatingAnimal
