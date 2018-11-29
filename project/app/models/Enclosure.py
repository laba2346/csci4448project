class Enclosure:
    id = 1

    def __init__(self,animals,foodType,cleanliness):
        """Initializes Enclosure object with unique id

        Args:
            animals (List<Animal>): List of animals to be included in enclosure
            foodType (string): description of food needed for enclosure
            cleanliness (string): Description of cleanliness of the enclosure
        Returns:
            None

        """
        self.animals = animals
        self.foodType = foodType
        self.cleanliness = "Clean"
        self.id = Enclosure.id
        self.numAnimals = len(self.animals)
        Enclosure.id += 1

    # Getters
    def getAnimals(self):
        """Gets the animals contained in enclosure

        Args:
            None
        Returns:
            List<Animal>: list of animals from enclosure

        """
        return self.animals

    def getNumAnimals(self):
        """Gets the number of animals in the enclosure

        Args:
            None
        Returns:
            int: Number of animals in enclosure

        """
        return self.numAnimals

    def getFoodType(self):
        """Gets the food type for the enclosure

        Args:
            None
        Returns:
            string: food type of enclosure

        """
        return self.foodType

    def getCleanliness(self):
        """Gets the cleanliness description of enclosure

        Args:
            None
        Returns:
            string: Describes cleanliness of enclosure

        """
        return self.cleanliness

    def getID(self):
        """Gets the unique ID of the enclosure

        Args:
            None
        Returns:
            int: enclosure's unique ID

        """
        return self.id

    # Setters
    def setAnimals(self, animals):
        """Sets the animal list to a new list

        Args:
            animals (List<Animal>): new animals for enclosure
        Returns:
            None

        """
        self.animals = animals

    def setFoodType(self, foodType):
        """Sets the food type to new value

        Args:
            foodType (string): new foodType
        Returns:
            None

        """
        self.foodType = foodType

    def setCleanliness(self, cleanliness):
        """Sets the cleanliness to a new value

        Args:
            cleanliness (string): new cleanlines value
        Returns:
            None

        """
        self.cleanliness = cleanliness

    def setNumAnimals(self, numAnimals):
        """Sets the number of animals in enclosure

        Args:
            numAnimals (int): new # of animals
        Returns:
            None

        """
        self.numAnimals = numAnimals

    def addAnimal(self, animal):
        """Adds an animal to the enclosure

        Args:
            animal (Animal): animal object to be added
        Returns:
            None

        """
        self.animals.append(animal)
        self.numAnimals += 1

    def removeAnimal(self, animalID):
        """Removes animal from enclosure by ID

        Args:
            animalID (int): ID of animal to be removed
        Returns:
            None

        """
        index = -1

        for i,animal in enumerate(self.animals):
            if int(animal.getID()) == int(animalID):
                print('hello')
                index = i
        if(index != -1):
            del self.animals[index]
            self.numAnimals -= 1
