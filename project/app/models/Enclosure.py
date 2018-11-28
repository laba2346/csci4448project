class Enclosure:
    id = 1

    def __init__(self,animals,foodType,cleanliness):
        self.animals = animals
        self.foodType = foodType
        self.cleanliness = "Clean"
        self.id = Enclosure.id
        self.numAnimals = len(self.animals)
        Enclosure.id += 1

    # Getters
    def getAnimals(self):
        return self.animals

    def getNumAnimals(self):
        return self.numAnimals

    def getFoodType(self):
        return self.foodType

    def getCleanliness(self):
        return self.cleanliness

    def getID(self):
        return self.id

    # Setters
    def setAnimals(self, animals):
        self.animals = animals

    def setFoodType(self, foodType):
        self.foodType = foodType

    def setCleanliness(self, cleanliness):
        self.cleanliness = cleanliness

    def setNumAnimals(self, numAnimals):
        self.numAnimals = numAnimals

    def addAnimal(self, animal):
        self.animals.append(animal)
        self.numAnimals += 1

    def removeAnimal(self, animalID):
        self.animals = [animal for animal in self.animals if animal.getID() != animalID]
        self.numAnimals -= 1
