from flask import Flask
from flask_pymongo import PyMongo
from whisk.config import Config

# variable for PyMongo
mongo = PyMongo()


# --------------------------------------- #
#    Create entire instance of the app    #
# --------------------------------------- #
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)

    # route imports
    from whisk.main.routes import main
    from whisk.recipes.routes import recipes
    from whisk.users.routes import users
    from whisk.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(recipes)
    app.register_blueprint(users)
    app.register_blueprint(errors)

    return app