from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

db =SQLAlchemy()

class Roles:
    ADMIN=os.getenv("ADMIN")
    CLIENT=os.getenv("CLIENT")
    SELLER=os.getenv("SELLER")


class User(db.Model):
    id = db.Column( db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    password= db.Column(db.String(50),nullable=False)
    email= db.Column(db.String(50),nullable=False)
    contact=db.Column(db.String(50),nullable=False)
    addres=db.Column(db.String(50),nullable=False)
    rol=db.Column(db.String(10),nullable=False,default=Roles.CLIENT)

    def __init__(self,name,password,contact,addres,email):
        self.name=name
        self.password=password
        self.email=email
        self.contact=contact
        self.addres=addres

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "password":self.password,
            "email":self.email,
            "contact":self.contact,
            "addres":self.addres,
            "rol":self.rol
        }


    def __repr__(self):
        return {"Name":self.name}