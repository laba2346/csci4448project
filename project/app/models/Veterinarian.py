from .Employee import Employee

class Veterinarian(Employee):
    def __init__(self, name, username, password, id, treatingAnimalID):
        super().__init__(name, username, password, id, "Veterinarian")
        self.treatingAnimalID = treatingAnimalID
        self.isTreatingAnimal = treatingAnimalID != -1

    def getTreatingAnimalID(self):
        return self.treatingAnimalID

    def getIsTreatingAnimal(self):
        return self.isTreatingAnimal

    def setTreatingAnimalID(self, treatingAnimalID):
        self.treatingAnimalID = treatingAnimalID

    def setIsTreatingAnimal(self, isTreatingAnimal):
        self.isTreatingAnimal = isTreatingAnimal
