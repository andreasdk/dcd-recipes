import os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

# ENVIRONMENT VARIABLES (.env)
app.config["MONGO_DBNAME"] = "whisk"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

from whisk import routes
