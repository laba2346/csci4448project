class SpeciesInfo:
    def __init__(self, name, description, diet, habitat, scientificName):
        self.name = name
        self.scientificName = scientificName
        self.description = description
        self.diet = diet
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

    def getScientificName(self):
        return self.scientificName

    # Setters
    def setDiet(self, diet):
        self.diet = diet

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description

    def setHabitat(self, habitat):
        self.habitat = habitat

    def setScientificName(self, scientificName):
        self.scientificName = scientificName
