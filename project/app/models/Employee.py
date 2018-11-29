from flask_login import UserMixin
from abc import ABC, abstractmethod
from .Credentials import Credentials
from .ContactInfo import ContactInfo

class Employee(ABC, UserMixin):
    id = 1
    def __init__(self, firstName, lastName, email, username, password, role):
        """Initalizes employee object. Creates contact info and credentials objects

        Args:
            firstName (string): First name of user
            lastName (string): Last name of user
            email (string): Email of user
            username (string): Username of user
            password (string): Password of user
            role (string): Name of role, "Veterinarian" or "Zookeeper"

        Returns:
            None

        """
        self.contactInfo = ContactInfo(firstName, lastName, email)
        self.credentials = Credentials(username, password)
        self.role = role
        self.id = Employee.id
        Employee.id += 1

    # Getters

    def get_id(self):
        """Gets the id (username) for the sake of flask_login

        Args:
            none
        Returns:
            string: Username of user

        """
        return self.credentials.getUsername()

    def getNumericID(self):
        """Gets the numeric ID (unique)

        Args:
            none
        Returns:
            int: Numeric ID of user

        """
        return self.id

    def getRole(self):
        """Gets the role of user

        Args:
            None
        Returns:
            string: User's role, Zookeeper or Veterinarian

        """
        return self.role

    def getCredentials(self):
        """Gets the credentials of the user

        Args:
            None
        Returns:
            Credentials: User's credentials, username/password.

        """
        return self.credentials

    def getContactInfo(self):
        """Gets the contact info of the user

        Args:
            None
        Returns:
            ContactInfo: user's contact information

        """
        return self.contactInfo

    @abstractmethod
    def getAssignmentID(self):
        pass

    def setCredentials(self, credentials):
        """Sets the credentials of the user

        Args:
            credentials (Credentials): new user credentials
        Returns:
            None

        """
        self.credentials = credentials

    def setRole(self, role):
        """Sets the role of the user

        Args:
            role (string): new user's role, Veterinarian or Zookeeper
        Returns:
            None

        """
        self.role = role

    def setContactInfo(self, contactInfo):
        """Sets the contact information of user

        Args:
            contactInfo (ContactInfo): new user contact info
        Returns:
            None

        """
        self.contactInfo = contactInfo

    @abstractmethod
    def removeAssignment(self):
        pass
