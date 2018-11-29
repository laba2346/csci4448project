class SpeciesInfo:
    def __init__(self, name, description, diet, habitat, scientificName):
        """Initializes the SpeciesInfo object

        Args:
            name (string): name of species
            description (string): short description of species
            diet (string): species' diet
            habitat (string): description of the habitat of the species
            scientificName (string): Scientific name of species
        Returns:
            None

        """
        self.name = name
        self.scientificName = scientificName
        self.description = description
        self.diet = diet
        self.habitat = habitat

    # Getters
    def getDiet(self):
        """Gets the species' diet

        Args:
            None
        Returns:
            string: Diet description

        """
        return self.diet

    def getName(self):
        """Gets the species' name

        Args:
            None
        Returns:
            string: Name of species

        """
        return self.name

    def getDescription(self):
        """Gets the description of the species

        Args:
            None
        Returns:
            string: description of species

        """
        return self.description

    def getHabitat(self):
        """Gets the habitat of the species

        Args:
            None
        Returns:
            string: Habitat description

        """
        return self.habitat

    def getScientificName(self):
        """Gets the scientific name of the species

        Args:
            None
        Returns:
            string: Scientific name of the species

        """
        return self.scientificName

    # Setters
    def setDiet(self, diet):
        """Sets the diet of the species

        Args:
            diet (string): new diet
        Returns:
            None

        """
        self.diet = diet

    def setName(self, name):
        """Sets the name of the species

        Args:
            name (string): new diet
        Returns:
            None

        """
        self.name = name

    def setDescription(self, description):
        """Sets the description of the species

        Args:
            description (string): new species description
        Returns:
            None

        """
        self.description = description

    def setHabitat(self, habitat):
        """Sets the habitat of the species

        Args:
            habitat (string): new habitat name
        Returns:
            None

        """
        self.habitat = habitat

    def setScientificName(self, scientificName):
        """Sets the scientific name of the species

        Args:
            description (string): new species scientific name
        Returns:
            None

        """
        self.scientificName = scientificName
