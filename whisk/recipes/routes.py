from flask import Flask, render_template, url_for, flash, redirect, request, session, Blueprint
from whisk import mongo
from whisk.utils import coll_recipes, coll_users
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from whisk.recipes.form import RecipeForm

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

    if request.method == 'POST':
        recipe = coll_recipes.insert_one({
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
            })
        coll_users.update_one({'_id': ObjectId(author)},
                              {'$push': {'user_recipes': recipe.inserted_id}})
        flash('Recipe Added!')
        return redirect(url_for('main.home'))



# ----- READ SINGLE RECIPE ----- #
@recipes.route('/recipes/<recipe_id>', methods=['GET', 'POST'])
def recipe(recipe_id):

    single_recipe = coll_recipes.find_one({"_id": ObjectId(recipe_id)})

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