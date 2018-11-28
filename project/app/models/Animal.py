from abc import ABC, abstractmethod

class Animal(ABC):
    id = 1

    def __init__(self, name, sex, age, healthy):
        self.name = name
        self.sex = sex
        self.age = age
        self.healthy = healthy
        self.id = Animal.id
        Animal.id += 1


    # Getters
    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def getAge(self):
        return self.age

    def getHealthy(self):
        return self.healthy

    def getHealthyEnglish(self):
        result = "Yes" if self.healthy else "No"

        return result

    # Setters
    def setName(self, name):
        self.name = name

    def setHealthy(self, healthy):
        self.healthy = healthy

    def setAge(self, age):
        self.age = age

    def setSex(self, sex):
        self.sex = sex

    @abstractmethod
    def getDetailedInfo(self):
        pass
