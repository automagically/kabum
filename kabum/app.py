from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from .models import db
from .schemas import ma
from .produto_controller import Produto


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mock.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)

ma.init_app(app)

api = Api(app)
api.add_resource(Produto, '/produtos')
