from flask import Blueprint, render_template, request
from whisk.utils import coll_recipes
from flask_pymongo import pymongo
import math

# --------------------- #
#    Flask Blueprint    #
# --------------------- #
main = Blueprint('main', __name__)


# ---------------- #
#    APP ROUTES    #
# ---------------- #

# ----- HOME ----- #
@main.route("/")
@main.route("/home")
def home():

    """
    Homepage, 8 random recipes from collection are displayed 
    as cards - each linking to individual recipe
    """

    random_recipes = (
        [recipe for recipe in coll_recipes.aggregate([
            {"$sample": {"size": 8}}])])

    return render_template('home.html', random_recipes=random_recipes, title="Whisk", )