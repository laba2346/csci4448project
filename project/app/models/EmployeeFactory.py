from .Zookeeper import Zookeeper
from .Veterinarian import Veterinarian

class EmployeeFactory:
    def getEmployee(self, name, username, password, id, role, preferredSpecies, treatingAnimalID):
        if(role == "Zookeeper"):
            return Zookeeper(name, username, password, id, preferredSpecies)
        elif(role == "Veterinarian"):
            return Veterinarian(name, username, password, id, treatingAnimalID)

        return None
