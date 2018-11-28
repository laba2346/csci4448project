from flask_login import UserMixin
from abc import ABC, abstractmethod
from .Credentials import Credentials

class Employee(ABC, UserMixin):

    def __init__(self, contactInfo, credentials, id, role):
        self.contactInfo = contactInfo
        self.credentials = credentials
        self.id = id
        self.role = role

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
