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

    per_page = 4
    current_page = int(request.args.get('current_page', 1))
    total = coll_recipes.count()
    pages = range(1, int(math.ceil(total / per_page)) + 1)
    recipes = coll_recipes.find().sort('_id', pymongo.DESCENDING).skip(
        (current_page - 1)*per_page).limit(per_page)

    return render_template('home.html', recipes=recipes, title="Whisk", current_page=current_page, pages=pages)