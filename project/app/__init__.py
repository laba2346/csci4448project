from flask import Flask
from config import Config
from app.models.Enclosure import Enclosure
from app.models.Zoo import Zoo
from app.models.Monkey import *
from app.models.Gorilla import *
from app.models.PolarBear import *
from app.models.Zookeeper import Zookeeper
from app.models.Veterinarian import Veterinarian
from app.models.AnimalFactory import AnimalFactory
from app.models.SpeciesInfo import SpeciesInfo
from flask_login import LoginManager

app = Flask(__name__)
login = LoginManager()
login.init_app(app)

# Initialize the controllers & zoo object

login.login_view = 'login'

jimbo = AnimalFactory.getAnimal("Jimbo", "Male", 3, True, "Monkey", {'canClimbTrees':"Yes"})
max = AnimalFactory.getAnimal("Max", "Male", 1.5, False, "Monkey", {'canClimbTrees':"No"})
bob = AnimalFactory.getAnimal("Bob", "Male", 3, False, "Gorilla", {'friendlyEnough':"Yes"})
fluffy = AnimalFactory.getAnimal("Fluffy", "Female", 2, True, "Polar bear", {'canReproduce':"Yes"})

enclosure_1 = Enclosure([fluffy], "Fish", "Clean")
enclosure_2 = Enclosure([jimbo, max, bob], "Fruit & Nuts", "Clean")

landon = Zookeeper("Landon", "Baxter", "landon.baxter@colorado.edu", "landon", "password", Monkey.getSpeciesInfo(), enclosure_1)
landonvet = Veterinarian("Landon", "Baxter", "landon.baxter@colorado.edu", "landonvet", "password",max)

zoo = Zoo([enclosure_1, enclosure_2],[landon,landonvet])

from app import routes

app.config.from_object(Config)
