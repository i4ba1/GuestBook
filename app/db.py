from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/guest_db"
mongo = PyMongo(app)

def initialize_db(app):
    db.init_app(app)
