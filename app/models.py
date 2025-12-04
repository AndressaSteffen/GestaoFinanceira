from flask_sqlalchemy import SQLAlchemy
from flask import UserMixin

db= SQLAlchemy()

class user (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key= True)
    username =db.Column (db.string(100), unique= True, nullable=False)
    email=db.Column (db.string(120), unique= True, nullable=False)
    password= db.Column (db.string(200), nullable=False)