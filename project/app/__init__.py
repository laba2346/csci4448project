from flask import Flask
from config import Config
from app.controllers.ZooController import ZooController
from app.controllers.UserController import UserController
from flask_login import LoginManager

app = Flask(__name__)
login = LoginManager()
login.init_app(app)

# Initialize the controllers & zoo object
zooController = ZooController()
zooController.createZoo()
userController = UserController()

login.login_view = 'login'

from app import routes

app.config.from_object(Config)
