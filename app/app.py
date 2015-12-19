# import packages
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


# import app configurations
from config import *


## App initiallization
app = Flask(__name__)
app.secret_key = SECRET_KEY


# Database initiallization
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


# Login manager initiallization
login_manager = LoginManager()
login_manager.init_app(app)


# import app views and models
from views import *
from models import *


## Create the database and commit the changes
db.create_all()
db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
