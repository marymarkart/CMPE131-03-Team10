from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
<<<<<<< Updated upstream

=======
 
>>>>>>> Stashed changes
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
basedir = os.path.abspath(os.path.dirname(__file__))

<<<<<<< Updated upstream
myapp_obj = Flask(__name__)

myapp_obj.config.from_mapping(
   SECRET_KEY = 'you-will-never-guess',
   SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
)

db = SQLAlchemy(myapp_obj)

from app import routes, models


=======
flaskObj = Flask(__name__)

 
flaskObj.config.from_mapping(
  SECRET_KEY = 'you-will-never-guess',
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
)
 
db = SQLAlchemy(flaskObj)
 
from app import routes, models
>>>>>>> Stashed changes
