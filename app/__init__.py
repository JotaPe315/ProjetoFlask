from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mulher-no-volante-perigo-constante'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
csrf = CSRFProtect(app)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.controllers import default
