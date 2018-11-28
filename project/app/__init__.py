from flask import Flask
from config import Config
from app.models.Enclosure import Enclosure
from app.models.Zoo import Zoo
from app.models.EmployeeFactory import EmployeeFactory
from app.models.AnimalFactory import AnimalFactory
from app.models.SpeciesInfo import SpeciesInfo
from flask_login import LoginManager

app = Flask(__name__)
login = LoginManager()
login.init_app(app)

# Initialize the controllers & zoo object
monkeyDiet = "Nuts and bananas"
monkeyDescription = "Cute and cuddly. Great at climbing trees and throwing poop"
monkeyHabitat = "Jungle"
monkeyScientificName = "Macaca Fascicularis"

monkeyInfo = SpeciesInfo("Monkey", monkeyDescription, monkeyDiet, monkeyHabitat, monkeyScientificName)

gorillaDiet = "Berries and nuts"
gorillaDescription = "Close relatives of the human, but much more dangerous."
gorillaHabitat = "Jungle"
gorillaScientificName = "Troglodytes Gorilla"

gorillaInfo = SpeciesInfo("Gorilla", gorillaDescription, gorillaDiet, gorillaHabitat, gorillaScientificName)


polarBearDiet = "Fish"
polarBearDescription = "Majestic, strong, but endangered."
polarBearHabitat = "Polar"
polarBearScientificName = "Ursus maritimus"

polarBearInfo = SpeciesInfo("Polar bear", polarBearDescription, polarBearDiet, polarBearHabitat, polarBearScientificName)

speciesList = [monkeyInfo, gorillaInfo, polarBearInfo] #these are declared in SpeciesInfo.py
jimbo = AnimalFactory.getAnimal("Jimbo", "Male", 3, True, "Monkey", {'canClimbTrees':"Yes"})
max = AnimalFactory.getAnimal("Max", "Male", 1.5, False, "Monkey", {'canClimbTrees':"No"})
bob = AnimalFactory.getAnimal("Bob", "Male", 3, False, "Gorilla", {'friendlyEnough':"Yes"})
pooh = AnimalFactory.getAnimal("Pooh", "Male", 1, True, "Polar bear", {'canReproduce':"Yes"})

enclosure_1 = Enclosure([jimbo, max, bob], "Fruit & Nuts", "Clean")
enclosure_2 = Enclosure([pooh], "Fish", "Clean")

zoo = Zoo([enclosure_1, enclosure_2],[],speciesList)

login.login_view = 'login'

from app import routes

app.config.from_object(Config)
