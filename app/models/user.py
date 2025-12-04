from app import db 
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id= db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(150),Unique=True,nullable=False)
    password= db.column(db.String(200),nullable=False)

