from .Animal import Animal

class Gorilla(Animal):
    def __init__(self, name, sex, age, healthy):
        diet = "Berries and nuts"
        description = "Close relatives of the human, but much more dangerous."
        habitat = "Jungle"
        super().__init__(name, sex, age, healthy, diet, "Gorilla", description, habitat)
        self.friendlyEnough = False # Friendly enough for small enclosures w/ others

    def getFriendlyEnough(self):
        return self.friendlyEnough

    def setFriendlyEnough(self, friendlyEnough):
        self.friendlyEnough = friendlyEnough
