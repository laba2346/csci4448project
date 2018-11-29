class Credentials:
    def __init__(self, username, password):
        """Initializes the credentials objet

        Args:
            username (string): Username
            password (string): user password
        Returns:
            string: The username

        """
        self.username = username
        self.password = password

    def getUsername(self):
        """Gets the credentials' username

        Args:
            None
        Returns:
            string: The username

        """
        return self.username

    def getPassword(self):
        """Gets the credentials' password

        Args:
            None
        Returns:
            string: The password

        """
        return self.password

    def checkPassword(self, password):
        """Checks a password against the stored one

        Args:
            password (string): The submitted password
        Returns:
            bool: True if password is correct, False otherwise

        """
        return password == self.password

    def setUsername(self, username):
        """Sets the credentials' username

        Args:
            username (string): New username
        Returns:
            None

        """
        self.username = username

    def setPassword(self, password):
        """Sets the credentials' password

        Args:
            password (string): New password
        Returns:
            None

        """
        self.password = password
