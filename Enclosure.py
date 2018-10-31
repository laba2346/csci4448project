class Enclosure:
    def __init__(self, animals, foodType, cleanliness):
        self.animals = animals
        self.foodType = foodType
        self.cleanliness = cleanliness
        self.assignedKeeper = None

    # Getters
    def getAnimals(self):
        return self.animals

    def getFoodType(self):
        return self.foodType

    def getCleanliness(self):
        return self.cleanliness

    def getAssignedKeeper(self):
        return self.assignedKeeper


    # Setters
    def setAnimals(self, animals):
        self.animals = animals

    def setFoodType(self, foodType):
        self.foodType = foodType

    def setCleanliness(self, cleanliness):
        self.cleanliness = cleanliness

    def setAssignedKeeper(self, assignedKeeper):
        self.assignedKeeper = assignedKeeper
