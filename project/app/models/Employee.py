from flask_login import UserMixin

class Employee(UserMixin):

    def __init__(self, name, username, password, id, role):
        self.name = name
        self.username = username
        self.password = password
        self.id = id
        self.role = role


    # Getters

    def getName(self):
        return self.name

    def get_id(self):
        return self.username

    def getRole(self):
        return self.role
    # def getCredentials(self):
    #     return self.credentials

    # def getContactInfo(self):
    #     return self.contactInfo

    def set_password(self, password):
        self.password = password

    def check_password(self, password):
        return password == self.password

    # Setters
    def setName(self, name):
        self.name = name

    # def setCredentials(self, credentials):
    #     self.credentials = credentials
    #
    # def setContactInfo(self, contactInfo):
    #     self.contactInfo = contactInfos
