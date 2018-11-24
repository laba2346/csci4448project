from .Animal import Animal

class PolarBear(Animal):
    def __init__(self, name, sex, age, healthy):
        diet = "Fish"
        description = "Majestic, strong, but endangered."
        habitat = "Polar"
        super().__init__(name, sex, age, healthy, diet, "Polar bear", description, habitat)
        self.canReproduce = True

    def getCanReproduce(self):
        return self.canReproduce

    def setCanReproduce(self, canReproduce):
        self.canReproduce = canReproduce
