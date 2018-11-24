from .Animal import Animal

class Monkey(Animal):
    def __init__(self, name, sex, age, healthy):
        diet = "Nuts and bananas"
        description = "Cute and cuddly. Great at climbing trees and throwing poop"
        habitat = "Jungle"
        super().__init__(name, sex, age, healthy, diet, "Monkey", description, habitat)
        self.canClimbTrees = True


    def getCanClimbTrees(self):
        return self.canClimbTrees

    def setCanClimbTrees(self, canClimbTrees):
        self.canClimbTrees = canClimbTrees
