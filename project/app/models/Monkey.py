from .Animal import Animal
from .SpeciesInfo import SpeciesInfo

class Monkey(Animal):
    speciesInfo = SpeciesInfo("Monkey", "Cute and cuddly. Great at climbing trees and throwing poop", "Nuts and bananas", "Jungle", "Macaca Fascicularis")

    def __init__(self, name, sex, age, healthy, canClimbTrees):
        """Initializes Monkey object, including the init of static variable speciesInfo

        Args:
            name (string): Name of animal
            sex (string): Sex of animal
            age (int): current age of animal
            healthy (bool): True or false
            canClimbTrees (bool): Indicates if monkey is mature enough enclosures w/ trees

        """
        super().__init__(name, sex, age, healthy)
        self.canClimbTrees = canClimbTrees == "Yes"

    def getCanClimbTrees(self):
        """Gets the monkey's ability to climb trees

        Args:
            None
        Returns:
            bool: Indicates if monkey can climb trees

        """
        return self.canClimbTrees

    def getCanClimbTreesEnglish(self):
        """Gets the monkey's ability to climb trees in English

        Args:
            None
        Returns:
            string: Indicates if monkey can climb trees, "Yes" or "No"

        """
        if(self.canClimbTrees):
            return "Yes"
        else:
            return "No"

    def setCanClimbTrees(self, canClimbTrees):
        """Sets the monkey's ability to climb trees

        Args:
            canClimbTrees (bool): New boolean describing monkey's ability to climb trees
        Returns:
            None

        """
        self.canClimbTrees = canClimbTrees

    def getDetailedInfo(self):
        """Gets an overview of the monkey's information, including their ability to climb trees

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
        info.append(("Old enough to climb trees safely?", self.getCanClimbTreesEnglish()))

        return info

    @staticmethod
    def getSpeciesInfo():
        """Static method that gets the monkey species information

        Args:
            None
        Returns:
            SpeciesInfo: species information for monkey

        """
        return Monkey.speciesInfo
