from abc import ABC, abstractmethod

class Animal(ABC):
    id = 1
    speciesInfo = None

    def __init__(self, name, sex, age, healthy):
        """Initializes the Animal object

        Args:
            name (string): Name of the animal
            sex (string): Male or Female
            age (int): Age of animal
            healthy (bool): Describes if the animal is healthy or not
        Returns:
            None

        """
        self.name = name
        self.sex = sex
        self.age = age
        self.healthy = healthy
        self.id = Animal.id
        Animal.id += 1


    # Getters
    def getID(self):
        """Gets the animal's ID

        Args:
            None
        Returns:
            int: The animal's ID

        """
        return self.id

    def getName(self):
        """Gets the animal's name

        Args:
            None
        Returns:
            string: The animal's name

        """
        return self.name

    def getSex(self):
        """Gets the animal's sex

        Args:
            None
        Returns:
            string: The animal's sex

        """
        return self.sex

    def getAge(self):
        """Gets the animal's age

        Args:
            None
        Returns:
            int: The animal's age

        """
        return self.age

    def getHealthy(self):
        """Gets the animal's healthy status

        Args:
            None
        Returns:
            bool: The animal's health status as a boolean

        """
        return self.healthy

    def getHealthyEnglish(self):
        """Returns the health status of the animal in english

        Args:
            None
        Returns:
            string: The animal's health status, "Yes" or "No"

        """
        result = "Yes" if self.healthy else "No"

        return result

    # Setters
    def setName(self, name):
        """Sets the animal's name

        Args:
            name (string): New name
        Returns:
            None

        """
        self.name = name

    def setHealthy(self, healthy):
        """Sets the animal's health status

        Args:
            healthy (bool): New health status
        Returns:
            None

        """
        self.healthy = healthy

    def setAge(self, age):
        """Sets the animal's age

        Args:
            age (int): New age
        Returns:
            None

        """
        self.age = age

    def setSex(self, sex):
        self.sex = sex

    @abstractmethod
    def getDetailedInfo(self):
        pass

    @abstractmethod
    def getSpeciesInfo(self):
        pass
