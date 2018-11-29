from .Employee import Employee

class Zookeeper(Employee):
    def __init__(self, firstName, lastName, email, username, password, preferredSpecies, assignedEnclosure):
        """Initializes the Zookeeper object

        Args:
            firstName (string): First name of user
            lastName (string): Last name of user
            email (string): Email of user
            username (string): Username of user
            password (string): Password of user
            preferredSpecies (SpeciesInfo): SpeciesInfo object of the species that the keeper prefers to work with
            assignedEnclosure (Enclosure): Enclosure object that the keeper is assigned to
        Returns:
            None

        """
        super().__init__(firstName, lastName, email, username, password, "Zookeeper")
        self.preferredSpecies = preferredSpecies
        self.assignedEnclosure = assignedEnclosure


    def getPreferredSpecies(self):
        """Gets the preferred species of keeper

        Args:
            None
        Returns:
            SpeciesInfo: info on preferred species

        """
        return self.preferredSpecies

    def getAssignedEnclosure(self):
        """Gets enclosure object that the keeper is assigned to

        Args:
            None
        Returns:
            Enclosure: enclosure that keeper is assigned to

        """
        return self.assignedEnclosure

    def getAssignmentID(self):
        """Gets the assignment ID of the keeper, specifically the ID of its assigned enclosure

        Args:
            None
        Returns:
            int: ID of assignedEnclosure. -1 if not assigned

        """
        if(self.assignedEnclosure is not None):
            return self.assignedEnclosure.getID()
        return -1

    def setPreferredSpecies(self, preferredSpecies):
        """Sets the keeper's preferred species

        Args:
            preferredSpecies (SpeciesInfo): new species info object
        Returns:
            None

        """
        self.preferredSpecies = preferredSpecies

    def setAssignedEnclosure(self, assignedEnclosure):
        """Sets the keeper's assigned enclosure

        Args:
            assignedEnclosure (Enclosure): new enclosure object to which keeper is assigned
        Returns:
            None

        """
        self.assignedEnclosure = assignedEnclosure

    def removeAssignment(self):
        """Removes the assignment to the keeper in case the enclosure is deleted or no longer needs it

        Args:
            none
        Returns:
            none

        """
        self.assignedEnclosure = None
