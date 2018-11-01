class Employee:
    id = 1

    def __init__(self, name, credentials, contactInfo):
        self.name = name
        self.credentials = credentials
        self.contactInfo = contactInfo
        self.id = Employee.id
        Employee.id += 1

    # Getters
    def getName(self):
        return self.name

    def getCredentials(self):
        return self.credentials

    def getContactInfo(self):
        return self.contactInfo

    # Setters
    def setName(self, name):
        self.name = name

    def setCredentials(self, credentials):
        self.credentials = credentials

    def setContactInfo(self, contactInfo):
        self.contactInfo = contactInfos
