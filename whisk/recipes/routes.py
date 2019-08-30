from flask import Flask, render_template, url_for, flash, redirect, request, session, Blueprint
from whisk import mongo
from whisk.utils import coll_recipes, coll_users
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from whisk.recipes.form import RecipeForm
import math

# --------------------- #
#    Flask Blueprint    #
# --------------------- #
recipes = Blueprint('recipes', __name__)


# ------------------------------------------- #
#    CRUD: Create | Read | Update | Delete    #
# ------------------------------------------- #


# ----- CREATE ----- #
@recipes.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():

    form = RecipeForm(request.form)
    user = coll_users.find_one({'username': session['username'
                               ].lower()})
    author = coll_users.find_one({"username": session["username"]})["_id"]

    

    if request.method == 'GET':
        return render_template('add_recipe.html', form=form,
                               title='Add Recipe')
    
    ingredients = request.form.get("ingredient_name").splitlines()
    directions = request.form.get("directions").splitlines()
    

    if request.method == 'POST':
        recipe = coll_recipes.insert_one({
            'recipe_name': request.form['recipe_name'],
            'description': request.form['description'],
            'meal_type': request.form['meal_type'],
            'diet_type': request.form['diet_type'],
            'prep_time': request.form['time'],
            'time': request.form['time'],
            'image': request.form['image'],
            'ingredient_name': ingredients,
            'directions': directions,
            'author': author,
            })
        coll_users.update_one({'_id': ObjectId(author)},
                              {'$push': {'user_recipes': recipe.inserted_id}})
        flash('Recipe Added!')
        return redirect(url_for('main.home'))

# ----- READ ALL RECIPES ----- #
@recipes.route('/recipes')
def all_recipes():

    per_page = 8
    current_page = int(request.args.get('current_page', 1))
    total = coll_recipes.count()
    pages = range(1, int(math.ceil(total / per_page)) + 1)
    recipes = coll_recipes.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*per_page).limit(per_page)

    return render_template('recipes.html', recipes=recipes, title="Recipes", current_page=current_page, pages=pages)

# ----- READ SINGLE RECIPE ----- #
@recipes.route('/recipes/<recipe_id>', methods=['GET', 'POST'])
def recipe(recipe_id):

    

    single_recipe = coll_recipes.find_one({"_id": ObjectId(recipe_id)})

    if 'logged_in' in session:
        user = coll_users.find_one({'username': session['username']})
        author = coll_users.find_one({'username': session['username'
                                 ]})['_id']
        return render_template('recipe.html', recipe=single_recipe,
                               title=single_recipe['recipe_name'],
                               user=user, author=author)
    else:

        return render_template('recipe.html',
                               recipe=single_recipe, title=single_recipe['recipe_name'])
       
# ----- UPDATE ----- #
@recipes.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):

    user = coll_users.find_one({'username': session['username']})  # Get the user

    selected_recipe = \
        coll_recipes.find_one({'_id': ObjectId(recipe_id)})  # Get the recipe

    author = coll_users.find_one({'username': session['username'
                                 ]})['_id']

    form = RecipeForm()  # Form

    if user['_id'] == selected_recipe['author']:

        form = RecipeForm(data=selected_recipe)

        if form.validate_on_submit():

            recipe = coll_recipes

            recipe.update_one({'_id': ObjectId(recipe_id)}, {'$set': {
                'recipe_name': request.form['recipe_name'],
                'description': request.form['description'],
                'meal_type': request.form['meal_type'],
                'allergens': request.form['allergens'],
                'prep_time': request.form['time'],
                'time': request.form['time'],
                'image': request.form['image'],
                'ingredient_name': request.form['ingredient_name'],
                'directions': request.form['directions'],
                'author': author,
                }})

            flash('Recipe successfully updated.')

            return redirect(url_for('recipes.recipe', recipe_id=recipe_id))
    else:

        flash("Sorry, you don't have the rights to edit this recipe!")

        return redirect(url_for('recipes.recipe', recipe_id=recipe_id))

    return render_template('edit_recipe.html', recipe=selected_recipe,
                           form=form, title='Edit Recipe')

# ----- DELETE ----- #
@recipes.route('/delete/<recipe_id>')
def delete_recipe(recipe_id):

    user = coll_users.find_one({'username': session['username']})  # Get the user

    selected_recipe = \
        coll_recipes.find_one({'_id': ObjectId(recipe_id)})  # Get the recipe
    
    author = coll_users.find_one({'username': session['username'
                                 ]})['_id']
    
    if user['_id'] == selected_recipe['author']:
        recipe = coll_recipes
        recipe.delete_one({
            '_id': ObjectId(recipe_id)
        })
        flash('Recipe deleted', 'success')
        return redirect(url_for('main.home'))

    flash("Sorry you can only delete your own recipes!")
    return redirect(url_for('recipes.recipe', recipe_id=recipe_id))

# ----- SEARCH ----- #
@recipes.route('/search')
def search():

    
    #  Results per page
    per_page = 8
    current_page = int(request.args.get('current_page', 1))
    #  Input term for search query
    search_query = request.args.get('search_query')
    #  Results for search sorted by ID
    results = coll_recipes.find({'$text': {'$search': str(search_query)}}, {"score": {"$meta": 'textScore'}}).sort('_id', pymongo.ASCENDING).skip((current_page -1)*per_page).limit(per_page)
    # Pagination
    results_count = coll_recipes.find({'$text': {'$search': str(search_query)}}).count()
    results_pages = range(1, int(math.ceil(results_count / per_page)) + 1)
    total_page_no = int(math.ceil(results_count/per_page))
    
    
    return render_template('search.html', 
                        per_page = per_page,
                        current_page=current_page, 
                        results_count=results_count,
                        search_query=search_query,
                        results=results,
                        results_pages=results_pages,
                        total_page_no=total_page_no,
                        )    
            
