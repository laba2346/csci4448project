class Credentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getUsername(self):
        return self.username

    def checkPassword(self, password):
        return password == self.password

    def setUsername(self):
        self.username = username

    def setPassword(self):
        self.password = password
