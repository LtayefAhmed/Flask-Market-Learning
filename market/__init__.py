from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'market.db')
app.config['SECRET_KEY'] = 'd3b21261d191903432e37855'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)




from market import routes
