class ContactInfo:
    def __init__(self, firstName, lastName, email):
        """Initializes the ContactInfo object for use with Employees

        Args:
            firstName (string): User's first name
            lastName (string): User's last name
            email (string): User's email
        Returns:
            None

        """
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

    def getFirstName(self):
        """Gets the contact's first name

        Args:
            None
        Returns:
            string: First name of contact

        """
        return self.firstName

    def getLastName(self):
        """Gets the contact's last name

        Args:
            None
        Returns:
            string: Last name of contact

        """
        return self.lastName

    def getEmail(self):
        """Gets the contact's email

        Args:
            None
        Returns:
            string: email of contact

        """
        return self.email

    def setFirstName(self, firstName):
        """Sets the contact's last name

        Args:
            firstName (string): New first name
        Returns:
            None

        """
        self.firstName = firstName

    def setLastName(self, lastName):
        """Sets the contact's last name

        Args:
            lastName (string): New last name
        Returns:
            None

        """
        self.lastName = lastName

    def setEmail(self, email):
        """Sets the contact's email

        Args:
            email (string): New email
        Returns:
            None

        """
        self.email = email
