from .Employee import Employee

class Veterinarian(Employee):
    def __init__(self, firstName, lastName, email, username, password, animalTreating):
        super().__init__(firstName, lastName, email, username, password, "Veterinarian")
        self.animalTreating = animalTreating
        self.isTreatingAnimal= animalTreating is not None

    def getIsTreatingAnimal(self):
        return self.isanimalTreating

    def getIsTreatingAnimalEnglish(self):
        return "Yes" if self.isTreatingAnimal else "No"

    def getAnimalTreating(self):
        return self.animalTreating

    def getAssignmentID(self):
        if(self.animalTreating is not None):
            return self.animalTreating.getID()
        return -1

    def setAnimalTreating(self, animalTreating):
        self.animalTreating = animalTreating

    def setIsTreatingAnimal(self, isTreatingAnimal):
        self.isanimalTreating = isTreatingAnimal

    def removeAssignment(self):
        self.animalTreating = None
