from flask import Flask

#initialization of application
from config import DevConfig

#initialization of application

app= Flask(__name__)
app= Flask(__name__, instance_relative_config = True)


#configuration set up
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views 