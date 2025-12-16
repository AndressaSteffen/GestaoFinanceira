from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

db=SQLAlchemy()

def create_app():
    app = Flask (__name__)

    app.config['SECRET_KEY'] = 'senha-secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gestao.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    db.init_app(app)

    from app.routes.auth import auth 
    app.register_blueprint(auth)
    return app
