from flask_login import UserMixin
from abc import ABC, abstractmethod
from .Credentials import Credentials
from .ContactInfo import ContactInfo

class Employee(ABC, UserMixin):
    id = 1
    def __init__(self, firstName, lastName, email, username, password, role):
        self.contactInfo = ContactInfo(firstName, lastName, email)
        self.credentials = Credentials(username, password)
        self.role = role
        self.id = Employee.id
        Employee.id += 1

    # Getters

    def get_id(self):
        return self.credentials.getUsername()

    def getNumericID(self):
        return self.id

    def getRole(self):
        return self.role

    def getCredentials(self):
        return self.credentials

    def getContactInfo(self):
        return self.contactInfo

    @abstractmethod
    def getAssignmentID(self):
        pass

    def setCredentials(self, credentials):
        self.credentials = credentials

    def setRole(self, role):
        self.role = role

    def setContactInfo(self, contactInfo):
        self.contactInfo = contactInfo

    @abstractmethod
    def removeAssignment(self):
        pass
