from .AnimalFactory import AnimalFactory
from .Enclosure import Enclosure
from .Monkey import Monkey
from .Gorilla import Gorilla
from .PolarBear import PolarBear

class Zoo:
    def __init__(self, enclosures, employees):
        """Initializes the zoo object

        Args:
            enclosures (List<Enclosure>): list of initial enclosures
            employees (List<Employee>): list of employees initially
        Returns:
            None
        """
        self.enclosures = enclosures
        self.employees = employees
        self.speciesList = [Monkey.getSpeciesInfo(), Gorilla.getSpeciesInfo(), PolarBear.getSpeciesInfo()]

    def addEnclosure(self, enclosure):
        """Adds a new enclosure to the zoo

        Args:
            enclosure (Enclosure): the enclosure to be added
        Returns:
            None

        """
        self.enclosures.append(enclosure)

    def removeEnclosure(self, enclosureID):
        """Removes an enclosure from the zoo. All animals in enclosure are also removed

        Args:
            enclosureID (int): the ID of enclosure to be deleted
        Returns:
            None

        """
        index = -1
        for i,enclosure in enumerate(self.enclosures):
            if int(enclosure.getID()) == int(enclosureID):
                index = i
        if(index != -1):
            for employee in self.employees:
                if(employee.getRole() == "Zookeeper"):
                    if(int(employee.getAssignmentID()) == int(enclosureID)):
                        employee.removeAssignment()
            del self.enclosures[index]


    def getEnclosures(self):
        """Gets list of all enclosures in zoo

        Args:
            None
        Returns:
            List<Enclosure>: all enclosures currently in zoo

        """
        return self.enclosures

    def getEnclosureByID(self, desiredID):
        """Gets enclosure by numeric ID

        Args:
            desiredID (int): Enclosure to be found
        Returns:
            Enclosure: desired enclosure

        """
        for enclosure in self.enclosures:
            if(enclosure.getID() == desiredID):
                return enclosure
        return None

    def addAnimalToEnclosure(self, animal, enclosureID):
        """Add animal to enclosure

        Args:
            animal (Animal): new animal to be added
            enclosureID (int): numeric ID of enclosure that is being added to
        Returns:
            None

        """
        for e in self.enclosures:
            if(enclosureID == e.getID()):
                e.addAnimal(animal)

    def removeAnimalFromEnclosure(self, enclosureID, animalID):
        """Removes an animal from an enclosures (and the zoo/employees as a result)

        Args:
            enclosureID (int): Numeric ID where animal is kept
            animalID (int): ID of animal to be removed
        Returns:
            None

        """
        animalID = int(animalID)
        enclosureID = int(enclosureID)
        for i in range(0, len(self.enclosures)):
            if(self.enclosures[i].getID() == enclosureID):
                self.enclosures[i].removeAnimal(animalID)

        for employee in self.employees:
            if(employee.getRole() == "Veterinarian" and employee.getAssignmentID() == animalID):
                employee.removeAssignment()

    def getAnimalByID(self, desiredID):
        """Gets an animal in zoo by numeric ID

        Args:
            desiredID (int): ID of desired animal
        Returns:
            Animal: desired animal object

        """
        for enclosure in self.enclosures:
            animals = enclosure.getAnimals()
            for animal in animals:
                if(int(animal.getID()) == int(desiredID)):
                    return animal
        return None

    def getSpeciesList(self):
        """Gets the list of species objects that the zoo contains

        Args:
            None
        Returns:
            List<SpeciesInfo>: all species allowed in zoo

        """

        return self.speciesList

    def getEmployees(self):
        """Gets the list of employees signed up for the zoo

        Args:
            None
        Returns:
            List<Employee>: list of all employees in zoo
        """
        return self.employees

    def setEmployees(self, employees):
        """Sets the list of employees to new list

        Args:
            employees (List<Employee>): list of new employees
        Returns:
            None
        """
        self.employees = employees
