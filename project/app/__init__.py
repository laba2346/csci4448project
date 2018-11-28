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

from app import routes

app.config.from_object(Config)
