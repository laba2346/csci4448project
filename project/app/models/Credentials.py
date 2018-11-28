class Credentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def checkPassword(self, password):
        return password == self.password

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password
