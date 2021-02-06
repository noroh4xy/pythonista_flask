from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


pythonista = Flask(__name__)
pythonista.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
pythonista.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
pythonista.config['SECRET_KEY'] = 'pythonista'
db = SQLAlchemy(pythonista)
migrate = Migrate(app=pythonista, db=db)

login_manager = LoginManager()
login_manager.init_app(app=pythonista)

from application import models, views

if __name__ == '__main__':
    pythonista.run(debug=True)