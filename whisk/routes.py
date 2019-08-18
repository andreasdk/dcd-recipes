from flask import Flask, render_template, url_for, flash, redirect, request, session
from whisk import app, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from whisk.forms import LoginForm, RegistrationForm, RecipeForm
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import random

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
#User registration function
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        user = mongo.db.user
        dup_user = user.find_one({'username': request.form['username'].lower()})

        avatars = [
            "apple", "watermelon", "pear", "grapes",
            "pomegranate", "orange", "pineapple", "lemon",
            "strawberry"]
        user_avatar = random.choice(avatars)

        if dup_user is None:
            hash_pass = generate_password_hash(request.form['password'])
            
            user.insert_one({'username': request.form['username'].lower(),
                             'pass': hash_pass, 'user_avatar': user_avatar})
            session['username'] = request.form['username']
            session['logged_in'] = True
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('home'))

        flash('Sorry, username already taken. Please try another.')
        return redirect(url_for('register'))
    return render_template('register.html', form=form, title="Register")


@app.route('/login', methods=['GET', 'POST'])
#User login function
def login():
    
    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.user
        existing_user = user.find_one({
                                'username': request.form['username'].lower()})
        # checks that hashed password matches user input
        if existing_user:
            if check_password_hash(existing_user['pass'],
                                   request.form['password']):
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('home'))
       
            #  else if invalid username/password match    
            flash('Login Unsuccessful. Please check email and password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form, title='Login')

@app.route('/account/<username>')
# User account page after login
def account(username):
    
    current_user = mongo.db.user.find_one({'username': username})

    return render_template('account.html', current_user=current_user, title="My Account")



@app.route('/logout')
# Ends session and redirects to homepage
def logout():
    # Ends session
    session.clear()  
    return redirect(url_for('home'))

# ------------------------------------------- #
#    CRUD: Create | Read | Update | Delete    #
# ------------------------------------------- #


# ----- CREATE ----- #
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():

    form = RecipeForm(request.form)
    user = mongo.db.user.find_one({'name': session['username'].lower()})
    
    
    if request.method == "GET":
        return render_template('add_recipe.html', form=form, title="Add Recipe")

    if request.method == "POST":
        recipe = mongo.db.recipes.insert_one({
                            'recipe_name': request.form['recipe_name'],
                            'description': request.form['description'],
                            'meal_type': request.form['meal_type'],
                            'allergens': request.form['allergens'],
                            'prep_time': request.form['time'],
                            'time': request.form['time'],
                            'image': request.form['image'],
                            'ingredient_name': request.form['ingredient_name'],
                            'directions': request.form['directions'],
                            'author': mongo.db.user.find_one({'username': session['username']})['_id']
        })
        flash('Recipe Added!')
        return redirect(url_for('home'))

# ----- READ ----- #
@app.route('/recipe/<recipe_id>', methods=['GET', 'POST'])
def recipe(recipe_id):

    single_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    return render_template('recipe.html',
                               recipe=single_recipe, title=single_recipe['recipe_name'])
        
    