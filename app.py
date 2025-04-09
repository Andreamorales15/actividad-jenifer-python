from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask import session, flash
import os
from dotenv import load_dotenv
from flask_mail import Mail, Message
app = Flask(__name__)  
app.config['SECRET_KEY'] = 'elsenorx'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'andreatumina1m@gmail.com' 
app.config['MAIL_PASSWORD'] = 'xqipwosetvldafjz'    
app.config['MAIL_DEFAULT_SENDER'] = 'andreatumina1m@gmail.com'

mail = Mail(app)
CORS(app)
app.config["UPLOAD_FOLDER"] = "./static/img"
app.config["MONGODB_SETTINGS"] = [{
    "db": "Gestionpeliculas",
    "host": os.getenv("MONGO_URI"),
    "port": 27017
}]

db = MongoEngine(app)

from routers.genero import *
from routers.pelicula import * 
from routers.iniciodesesion import * 
from routers.actividadesdelusuario import * 
from routers.recuperarcuenta import * 

if __name__ == "__main__":
    app.run(port=6510, host="0.0.0.0", debug=True)
