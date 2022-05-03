from flask import Flask
from flask_bootstrap import Bootstrap

#initialization of application
from cconfig import DevConfig
bootstrap = Bootstrap()

#initialization of application

app= Flask(__name__)
app= Flask(__name__, instance_relative_config = True)


#configuration set up
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initializing bootstrap extension
bootstrap.init_app(app)

from app import views 