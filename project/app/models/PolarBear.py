from .Animal import Animal
from .SpeciesInfo import SpeciesInfo

class PolarBear(Animal):
    speciesInfo = SpeciesInfo("Polar bear", "Majestic, strong, but endangered.","Fish", "Polar", "Ursus maritimus")

    def __init__(self, name, sex, age, healthy, canReproduce):
        """Initializes Polar bear object, including the init of static variable speciesInfo

        Args:
            name (string): Name of animal
            sex (string): Sex of animal
            age (int): current age of animal
            healthy (bool): True or false
            canReproduce (bool): Indicates if polar bear is suitable for mating

        Returns:
            None
        """
        super().__init__(name, sex, age, healthy)
        self.canReproduce = canReproduce == "Yes"

    def getCanReproduce(self):
        """Gets the ability for animal to reproduce, boolean

        Args:
            None
        Returns:
            string: true or false

        """
        return self.canReproduce

    def getCanReproduceEnglish(self):
        """Gets the ability for animal to reproduce in English

        Args:
            None
        Returns:
            string: Yes or No

        """
        if(self.canReproduce):
            return "Yes"
        else:
            return "No"

    def setCanReproduce(self, canReproduce):
        """Sets the ability for polar bear to mate

        Args:
            canReproduce (bool): The bool describing the ability for mating
        Returns:
            None

        """
        self.canReproduce = canReproduce


    def getDetailedInfo(self):
        """Gets an overview of the polar bear's information, including their suitability for mating

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
        info.append(("Suitable for mating?", self.getCanReproduceEnglish()))

        return info

    @staticmethod
    def getSpeciesInfo():
        """Static method that gets the polar species information

        Args:
            None
        Returns:
            SpeciesInfo: species information for polar bears

        """
        return PolarBear.speciesInfo
