class Animal:
    id = 1

    def __init__(self, name, sex, age, healthy, diet, speciesName,
        speciesDescription, habitat):

        self.id = id
        self.name = name
        self.sex = sex
        self.age = age
        self.healthy = healthy
        self.diet = diet
        self.speciesName = speciesName
        self.speciesDescription = speciesDescription
        self.habitat = habitat
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

    def getSpeciesName(self):
        return self.speciesName

    def getSpeciesDescription(self):
        return self.speciesDescription

    # Setters
    def setName(self, name):
        self.name = name

    def setHealthy(self, healthy):
        self.healthy = healthy

    def setAge(self, age):
        self.age = age
