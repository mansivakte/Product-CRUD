import os
import bcrypt
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from .db import db
from .user.view import user_blueprint
from .product.view import product_blueprint

app = Flask(__name__,static_folder='uploads')
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+ os.path.join(basedir, 'data_sqlite.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db.init_app(app)
migrate = Migrate(app,db)
bcrypt = Bcrypt(app)

app.register_blueprint(user_blueprint)
app.register_blueprint(product_blueprint)