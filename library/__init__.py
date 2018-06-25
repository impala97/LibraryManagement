from flask import Flask
from flask_login import LoginManager


library = Flask(__name__)
session_manager = LoginManager()

from library.controllers import *
