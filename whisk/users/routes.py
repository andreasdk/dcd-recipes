from flask import Flask, render_template, url_for, flash, redirect, request, session, Blueprint
from whisk import mongo
from flask_pymongo import pymongo
from werkzeug.security import generate_password_hash, check_password_hash
from whisk.utils import coll_recipes, coll_users
import random
from bson.objectid import ObjectId
from whisk.users.form import RegistrationForm, LoginForm, PasswordForm, DeleteForm



# --------------------- #
#    Flask Blueprint    #
# --------------------- #
users = Blueprint('users', __name__)


# ------------------------------------------- #
#    USER: Regiser | Login | Profile | Logout #
# ------------------------------------------- #

# ----- REGISTER ----- #
@users.route('/register', methods=['GET', 'POST'])
#User registration function
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        user = coll_users
        dup_user = user.find_one({'username': request.form['username'].lower()})

        avatars = [
            "apple", "watermelon", "pear", "grapes",
            "pomegranate", "orange", "pineapple", "lemon",
            "strawberry"]
        user_avatar = random.choice(avatars)

        if dup_user is None:
            hash_pass = generate_password_hash(request.form['password'])
            
            user.insert_one({'username': request.form['username'].lower(),
                             'pass': hash_pass, 'user_avatar': user_avatar, "user_recipes": []})
            session['username'] = request.form['username']
            session['logged_in'] = True
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('main.home'))

        flash('Sorry, username already taken. Please try another.')
        return redirect(url_for('users.register'))
    return render_template('register.html', form=form, title="Register")


# ----- LOGIN ----- #
@users.route('/login', methods=['GET', 'POST'])
#User login function
def login():
    
    form = LoginForm()
    if form.validate_on_submit():
        user = coll_users
        existing_user = user.find_one({
                                'username': request.form['username'].lower()})
        # checks that hashed password matches user input
        if existing_user:
            if check_password_hash(existing_user['pass'],
                                   request.form['password']):
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('main.home'))
       
            #  else if invalid username/password match    
            flash('Login Unsuccessful. Please check email and password', 'danger')
            return redirect(url_for('users.login'))
    return render_template('login.html', form=form, title='Login')


# ----- USER PROFILE ----- #
@users.route('/account/<username>', methods=["GET", "POST"])
# User account page after login
def account(username):

    username = coll_users.find_one({'username': session['username']})['username']
    user_id = coll_users.find_one({'username': session['username']})['_id']
    user_avatar = coll_users.find_one({'username': session['username']})['user_avatar']
    user_recipes = coll_recipes.find({'author': user_id}).sort([('recipe_name', 1)])
    form=DeleteForm()

    return render_template('account.html', username=username, user_avatar=user_avatar, user_recipes=user_recipes, form=form, title="My Account")

# ----- UPDATE PASSWORD ----- #
@users.route('/edit/<username>/', methods=['GET', 'POST'])
def update_password(username):

    username = coll_users.find_one({'username': session['username'
                                   ]})['username']
    form = PasswordForm()

    if form.validate_on_submit():

        form = PasswordForm(username)

        if check_password_hash(coll_users.find_one({'username': username})['pass'
                               ], request.form.get('current_password')):
            coll_users.update_one({'username': username},
                                  {'$set': {'pass': generate_password_hash(request.form.get('new_password'
                                  ))}})
            return redirect(url_for('users.account', username=username))

        else:
            flash("Original password is incorrect!")
            return redirect(url_for(
                "users.update_password",
                username=username))

    return render_template('change_password.html', username=username,
                           form=form, title='Change Password')

# ----- DELETE ACCOUNT ----- #
@users.route('/profile/<username>/delete', methods=['GET', 'POST'])
def delete_account(username):

    username = coll_users.find_one({'username': session['username'
                                   ]})['username']
    form = DeleteForm()

    if form.validate_on_submit():

        form = DeleteForm(username)

        if check_password_hash(coll_users.find_one({'username': username})['pass'
                               ], request.form.get('verify_password')):
         # find all recipes belonging to user
            user_recipes = username.get('user_recipes')

        # for each user recipe, remove from database

            for recipe in user_recipes:
                coll_recipes.remove({'_id': recipe})

        # end session and delete user from database

       session.clear())
        coll_users.remove({'_id': user.get('_id')})
        return redirect(url_for('main.home'))

    return render_template('delete_account.html', username=username,
                           form=form, title='Account')



# ----- LOGOUT ----- #
@users.route('/logout')
# Ends session and redirects to homepage
def logout():
    # Ends session
    session.clear()  
    return redirect(url_for('main.home'))