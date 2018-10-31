class Employee:
    id = 0

    def __init__(self, name, username, password, contactInfo):
        self.name = name
        #TODO make new credentials obj
        #TODO make new contactInfo obj
        self.contactInfo = contactInfo
        self.id = id
        id += 1

    # Getters
    def getName(self):
        return self.name

    def getCredentials(self):
        return self.credentials

    def getContactInfo(self):
        retiurn self.contactInfo

    # Setters
    def setName(self, name):
        self.name = name

    def setCredentials(self, credentials):
        self.credentials = credentials

    def setContactInfo(self, contactInfo):
        self.contactInfo = contactInfos
