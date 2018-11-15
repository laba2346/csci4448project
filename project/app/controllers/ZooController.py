from ..models.Animal import *
from ..models.Species import *
from ..models.Zoo import *
from ..models.Employee import *
from ..models.Enclosure import *

class ZooController:
    def createZoo(self):
        monkey = Species("Fruits & nuts", "Monkey", "Very curious and slightly dangerous animal", "Jungle")
        gorilla = Species("Fruits & nuts", "Gorilla", "Big monkey, slightly more dangerous", "Jungle")
        polar_bear = Species("Fish", "Polar Bear", "Very large and cuddly looking bear; prefers the cold.", "Polar")
        species_list = [monkey, gorilla, polar_bear]

        jimbo = Animal("Jimbo", "M", monkey, 3, True)
        max = Animal("Max", "M", monkey, 1.5, True)
        bob = Animal("Bob", "M", gorilla, 3, False)
        pooh = Animal("Pooh", "M", polar_bear, 1, True)

        enclosure_1 = Enclosure([jimbo, max, bob], "Fruit & Nuts", "Clean")
        enclosure_2 = Enclosure([pooh], "Fish", "Clean")

        zoo = Zoo([enclosure_1, enclosure_2],[],[monkey, gorilla, polar_bear])

        return zoo
