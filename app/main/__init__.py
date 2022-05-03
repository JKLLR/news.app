from ensurepip import bootstrap
from flask import Blueprint, Flask
main = Blueprint('main', __name__)
from . import views, errors


def create_app(config_name):
   app= Flask(__name__)

   # creating app configurations

   # app.config.from_object(config_options [config_name])

   # Initializing flask extensions

   bootstrap.init_app(app)

   # registering the blueprint

   from ..main import main as main_blueprint
   app.register_blueprint(main_blueprint)

   return app