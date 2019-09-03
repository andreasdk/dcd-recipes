from flask import Flask, render_template, url_for, flash, redirect, \
    request, session, Blueprint
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

    """
    Add recipe function that calls the RecipeForm class from recipes/form.py
    Only logged in users can create recipes. Assigns an author to each recipe.
    """
    # Checks if user is logged in
    if 'logged_in' not in session:  
        flash('Sorry, you must be logged in to create a recipe.')
        return redirect(url_for('main.home'))
    # Form variable set as RecipeForm from recipes/form.py
    form = RecipeForm(request.form)
    # Gets user and author details
    user = coll_users.find_one({'username': session['username'
                               ].lower()})                       
    author = coll_users.find_one({"username": session["username"]})["_id"]

    

    if request.method == 'GET':
        # Renders template and form
        return render_template('add_recipe.html', form=form,
                               title='Add Recipe')
    
    ingredients = request.form.get("ingredient_name").splitlines()
    directions = request.form.get("directions").splitlines()
    

    if request.method == 'POST':
        # Creates new recipe with form data
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
        # User is found with author id, user recipes
        # updated with recipe id
        coll_users.update_one({'_id': ObjectId(author)},
                              {'$push': {'user_recipes': recipe.inserted_id}})
        flash('Recipe Added!')
        return redirect(url_for('main.home'))

# ----- READ ALL RECIPES ----- #
@recipes.route('/recipes')
def all_recipes():

    """
    Displays all recipes from database. Pagination
    sets limit of displayed recipes to 8 per page.
    """

    per_page = 8
    current_page = int(request.args.get('current_page', 1))
    total = coll_recipes.count()
    pages = range(1, int(math.ceil(total / per_page)) + 1)
    recipes = coll_recipes.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*per_page).limit(per_page)

    return render_template('recipes.html', recipes=recipes, title='Recipes'
                       , current_page=current_page, pages=pages)

# ----- READ SINGLE RECIPE ----- #
@recipes.route('/recipes/<recipe_id>', methods=['GET', 'POST'])
def recipe(recipe_id):

    """
    Read a single recipe from collection. If logged in user id matches
    recipe author, user has option to edit or delete recipe.
    """

    # Finds recipe in collection based on id
    single_recipe = coll_recipes.find_one({"_id": ObjectId(recipe_id)})

    # If logged in user set to session username, author set to session user id
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

    """
    Edit recipe function that calls the RecipeForm class from recipes/form.py
    Only recipe author can edit a recipe.
    """
    # Get the user
    user = coll_users.find_one({'username': session['username']})  
    # Get the recipe
    selected_recipe = \
        coll_recipes.find_one({'_id': ObjectId(recipe_id)})  
    # Get the author
    author = coll_users.find_one({'username': session['username'
                                 ]})['_id']
    # Defines the form as the RecipeForm class from recipes/form.py 
    form = RecipeForm() 
    # If user id matched author of recipe
    if user['_id'] == selected_recipe['author']:
        # Recipe form is population with the recipe data
        form = RecipeForm(data=selected_recipe)
        # If form correctly validates
        if form.validate_on_submit():

            recipe = coll_recipes
            # Recipe is updated according to data in form
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

    """
    Delete recipe function. Only recipe author can delete recipe.
    """

    # Gets the user

    user = coll_users.find_one({'username': session['username']})

    # Gets the recipe
    selected_recipe = \
        coll_recipes.find_one({'_id': ObjectId(recipe_id)})
      
    # Gets the author
    author = coll_users.find_one({'username': session['username'
                                 ]})['_id']

    # If current user id matches the author id, recipe can be deleted
    if user['_id'] == selected_recipe['author']:
        recipe = coll_recipes
        recipe.delete_one({
            '_id': ObjectId(recipe_id)
        })
        flash('Recipe deleted', 'success')
        return redirect(url_for('main.home'))
    # else user gets a flash message and redirect back to the recipe page
    flash("Sorry you can only delete your own recipes!")
    return redirect(url_for('recipes.recipe', recipe_id=recipe_id))

# ----- SEARCH ----- #
@recipes.route('/search')
def search():

    """
    Allows a user to search for recipes. All fields in recipe are searchable
    due to Wildcard Index:
    coll_recipes.create_index([("$**", pymongo.TEXT)])
    """

    #  Results per page
    per_page = 8
    current_page = int(request.args.get('current_page', 1))

    #  Input term for search query
    search_query = request.args.get('search_query')

    #  Search results sorted by ID
    results = \
        coll_recipes.find({'$text': {'$search': str(search_query)}},
                          {'score': {'$meta': 'textScore'}}).sort('_id'
            , pymongo.ASCENDING).skip((current_page - 1)
            * per_page).limit(per_page)

    # Pagination
    results_count = \
        coll_recipes.find({'$text': {'$search': str(search_query)}}).count()
    results_pages = range(1, int(math.ceil(results_count / per_page))
                          + 1)
    total_pages = int(math.ceil(results_count / per_page))

    return render_template(
        'search.html',
        per_page=per_page,
        current_page=current_page,
        results_count=results_count,
        search_query=search_query,
        results=results,
        results_pages=results_pages,
        total_pages=total_pages,
        )

