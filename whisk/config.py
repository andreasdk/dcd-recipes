import os

# Config Settings & Environmental Variables
class Config:
    MONGO_DBNAME = "whisk"
    MONGO_URI = os.getenv("MONGO_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")
