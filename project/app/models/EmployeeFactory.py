from .Zookeeper import Zookeeper
from .Veterinarian import Veterinarian
from .ContactInfo import ContactInfo
from .Credentials import Credentials

class EmployeeFactory:
    @staticmethod
    def getEmployee(firstName, lastName, email, username, password, id, role, preferredSpecies, assignmentID):
        contactInfo = ContactInfo(firstName, lastName, email)
        credentials = Credentials(username, password)
        if(role == "Zookeeper"):
            return Zookeeper(contactInfo, credentials, id, preferredSpecies, assignmentID)
        elif(role == "Veterinarian"):
            return Veterinarian(contactInfo, credentials, id, assignmentID)

        return None
