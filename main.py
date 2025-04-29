from flask import Flask,request,redirect,url_for,jsonify
from db import db,User
from flask_cors import CORS

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"
db.init_app(app)

CORS(app)

@app.route("/")
def  index():
    return jsonify({"message":"Bienvenido a la API"})

@app.route("/register",methods=["POST"])
def register():
    data=request.get_json()
    name=data.get("nombre")
    password=data.get("contraseña")
    email=data.get("correo")
    contact=data.get("contacto")
    addres=data.get("direccion")
    user=User(name,password,contact,addres,email)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message":"User added Sucessfully"})


if __name__ =="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True,host="0.0.0.0")

