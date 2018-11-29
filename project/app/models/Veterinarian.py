from .Employee import Employee

class Veterinarian(Employee):
    def __init__(self, firstName, lastName, email, username, password, animalTreating):
        """Initializes the Veterinarian object

        Args:
            firstName (string): First name of user
            lastName (string): Last name of user
            email (string): Email of user
            username (string): Username of user
            password (string): Password of user
            animalTreating (Animal): animal that the vet is currently treating

        Returns:
            None

        """
        super().__init__(firstName, lastName, email, username, password, "Veterinarian")
        self.animalTreating = animalTreating
        self.isTreatingAnimal= animalTreating is not None

    def getIsTreatingAnimal(self):
        """Returns a bool indicating if the vet is treating an animal

        Args:
            None
        Returns:
            bool: True or False if treating an animal or not

        """
        return self.isanimalTreating

    def getIsTreatingAnimalEnglish(self):
        """Returns a string indicating if the vet is treating an animal

        Args:
            None
        Returns:
            string: Yes or No

        """
        return "Yes" if self.isTreatingAnimal else "No"

    def getAnimalTreating(self):
        """Returns the animal that is being treated by vet

        Args:
            None
        Returns:
            Animal: animal being treated by the vet

        """
        return self.animalTreating

    def getAssignmentID(self):
        """Gets the assignment ID of the vet, specifically the ID of its treating animal

        Args:
            None
        Returns:
            int: ID of animalTreating. -1 if not treating animal

        """
        if(self.animalTreating is not None):
            return self.animalTreating.getID()
        return -1

    def setAnimalTreating(self, animalTreating):
        """Sets the animal that the vet is treating

        Args:
            animalTreating (Animal):  new animal being treated
        Returns:
            None

        """
        self.animalTreating = animalTreating

    def setIsTreatingAnimal(self, isTreatingAnimal):
        """Sets the boolean that indicates if vet is treating animal

        Args:
            isTreatingAnimal (Animal): new boolean describing treatment
        Returns:
            None

        """
        self.isanimalTreating = isTreatingAnimal

    def removeAssignment(self):
        """Removes the assignment to the vet in case the animal is deleted or no longer needs it

        Args:
            none
        Returns:
            none
        """
        self.animalTreating = None
