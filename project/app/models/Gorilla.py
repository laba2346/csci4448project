from .Animal import Animal
from .SpeciesInfo import SpeciesInfo

class Gorilla(Animal):
    speciesInfo = SpeciesInfo("Gorilla","Close relatives of the human, but much more dangerous.","Berries and nuts","Jungle","Troglodytes Gorilla")

    def __init__(self, name, sex, age, healthy, friendlyEnough):
        """Initializes Gorilla object, including the init of static variable speciesInfo

        Args:
            name (string): Name of animal
            sex (string): Sex of animal
            age (int): current age of animal
            healthy (bool): True or false
            friendlyEnough (bool): Indicates if gorilla is friendly enough for enclosure with others

        Returns:
            None
        """
        super().__init__(name, sex, age, healthy)
        self.friendlyEnough = friendlyEnough == "Yes" # Friendly enough for small enclosures w/ others

    def getFriendlyEnough(self):
        """Gets the boolean describing friendliness of gorilla

        Args:
            None
        Returns:
            bool: True if friendly, False if not

        """
        return self.friendlyEnough

    def getFriendlyEnoughEnglish(self):
        """Gets the friendly description in english rather than bool

        Args:
            None
        Returns:
            string: Yes or No

        """
        if(self.friendlyEnough):
            return "Yes"
        else:
            return "No"

    def setFriendlyEnough(self, friendlyEnough):
        """Sets the friendliness of the gorilla

        Args:
            friendlyEnough (bool): The bool describing the new friendliness
        Returns:
            None

        """
        self.friendlyEnough = friendlyEnough

    def getDetailedInfo(self):
        """Gets an overview of the gorilla's information, including their friendliness

        Args:
            None
        Returns:
            List<(string, string)>: first element of tuple is label, second is the value

        """
        info = []
        info.append(("Name", self.name))
        info.append(("Sex", self.sex))
        info.append(("Age", self.age))
        info.append(("Healthy?", self.getHealthyEnglish()))
        info.append(("Species", self.getSpeciesInfo().getName()))
        info.append(("Friendly with other animals?", self.getFriendlyEnoughEnglish()))

        return info

    @staticmethod
    def getSpeciesInfo():
        """Static method that gets the gorilla species information

        Args:
            None
        Returns:
            SpeciesInfo: species information for gorilla

        """
        return Gorilla.speciesInfo
