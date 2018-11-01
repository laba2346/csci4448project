class Species:
    def __init__(self, diet, name, description, habitat):
        self.diet = diet
        self.name = name
        self.description = description
        self.habitat = habitat

    # Getters
    def getDiet(self):
        return self.diet

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getHabitat(self):
        return self.habitat

    # Setters
    def setDiet(self, diet):
        self.diet = diet

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description

    def setHabitat(self, habitat):
        self.habitat = habitat

    def printInformation():
        print("TODO")
