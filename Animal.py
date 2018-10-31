class Animal:
    def __init__(self, id, name, sex, species, age, Healthy):
        self.id = id
        self.name = name
        self.sex = sex
        self.species = species
        self.age = age
        self.healthy = healthy

    # Getters
    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def getSpecies(self):
        return self.species

    def getAge(self):
        return self.age

    def getHealthy(self):
        return self.healthy


    # Setters
    def setName(self, name):
        self.name = name

    def setHealthy(self, healthy):
        self.healthy = healthy

    def setAge(self, age):
        self.age = age
