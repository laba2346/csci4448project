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

login.login_view = 'login'

employeeFactory = EmployeeFactory()
animalFactory = AnimalFactory()

jimbo = AnimalFactory.getAnimal("Jimbo", "Male", 3, True, "Monkey", {'canClimbTrees':"Yes"})
max = AnimalFactory.getAnimal("Max", "Male", 1.5, False, "Monkey", {'canClimbTrees':"No"})
bob = AnimalFactory.getAnimal("Bob", "Male", 3, False, "Gorilla", {'friendlyEnough':"Yes"})
pooh = AnimalFactory.getAnimal("Pooh", "Male", 1, True, "Polar bear", {'canReproduce':"Yes"})

enclosure_1 = Enclosure([jimbo, max, bob], "Fruit & Nuts", "Clean")
enclosure_2 = Enclosure([pooh], "Fish", "Clean")

landon = employeeFactory.getEmployee("Landon", "Baxter", "landon.baxter@colorado.edu", "landon", "password",1,"Zookeeper","Monkey",1)
landonvet = employeeFactory.getEmployee("Landon", "Baxter", "landon.baxter@colorado.edu", "landonvet", "password",2,"Veterinarian","",2)

zoo = Zoo([enclosure_1, enclosure_2],[landon, landonvet])

from app import routes

app.config.from_object(Config)
