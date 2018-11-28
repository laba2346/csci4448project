from .Zookeeper import Zookeeper
from .Veterinarian import Veterinarian
from .ContactInfo import ContactInfo
from .Credentials import Credentials

class EmployeeFactory:
    def getEmployee(self, firstName, lastName, email, username, password, id, role, preferredSpecies, treatingAnimalID, assignedEnclosureID):
        contactInfo = ContactInfo(firstName, lastName, email)
        credentials = Credentials(username, password)
        if(role == "Zookeeper"):
            return Zookeeper(contactInfo, credentials, id, preferredSpecies, assignedEnclosureID)
        elif(role == "Veterinarian"):
            return Veterinarian(contactInfo, credentials, id, treatingAnimalID)

        return None
