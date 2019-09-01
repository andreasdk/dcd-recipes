from flask import Flask, render_template, url_for, flash, redirect, \
    request, session, Blueprint
from whisk import mongo
from flask_pymongo import pymongo
from werkzeug.security import generate_password_hash, \
    check_password_hash
from whisk.utils import coll_recipes, coll_users
import random
from bson.objectid import ObjectId
from whisk.users.form import RegistrationForm, LoginForm, PasswordForm

# --------------------- #
#    Flask Blueprint    #
# --------------------- #

users = Blueprint('users', __name__)


# ------------------------------------------- #
#    USER: Regiser | Login | Profile | Logout #
# ------------------------------------------- #

# ----- REGISTER ----- #
# User registration function

@users.route('/register', methods=['GET', 'POST'])
def register():
    """
    Registration function that calls the RegistrationForm class
    from user/form.py.Checks if username is unique, hashes password,
    assigns random avatar to user,
    and sets user_recipes to empty array.
    """

    form = RegistrationForm()

    if form.validate_on_submit():

        # Sets user collection variable

        user = coll_users

        # Searches the user collection to check if username exists

        dup_user = user.find_one({'username': request.form['username'
                                 ].lower()})

        # Assigns a random avatar to user
        # Avatars are PNG files stored in static/img/avatars

        avatars = [
            'apple',
            'watermelon',
            'pear',
            'grapes',
            'pomegranate',
            'orange',
            'pineapple',
            'lemon',
            'strawberry',
            ]
        user_avatar = random.choice(avatars)

        # If username does not already exist in collection

        if dup_user is None:

            # Hashes password

            hash_pass = generate_password_hash(request.form['password'])

            # Inserts a new user entry into collection

            user.insert_one({
                'username': request.form['username'].lower(),
                'pass': hash_pass,
                'user_avatar': user_avatar,
                'user_recipes': [],
                })

            # Session username is set to username entered in form

            session['username'] = request.form['username']

            # User is set as logged in

            session['logged_in'] = True
            flash('Your account has been created! You are now able to log in'
                  )
            return redirect(url_for('main.home'))

        flash('Sorry, username already taken. Please try another.')
        return redirect(url_for('users.register'))
    return render_template('register.html', form=form, title='Register')


# ----- LOGIN ----- #
# User login function

@users.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login function that calls the LoginForm class from users/form.py
    Checks if username and password match an entry in user collection.
    """

    form = LoginForm()

    if form.validate_on_submit():

        # Sets user collection variable

        user = coll_users

        # Search for existing user in user collection

        existing_user = \
            user.find_one({'username': request.form['username'
                          ].lower()})

        # Checks that hashed password matches user input

        if existing_user:
            if check_password_hash(existing_user['pass'],
                                   request.form['password']):
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('main.home'))

            #  Else if invalid username/password match

            flash('Login Unsuccessful. Please check username and password'
                  )
            return redirect(url_for('users.login'))
    return render_template('login.html', form=form, title='Login')


# ----- USER ACCOUNT PAGE ----- #
# User account page after login

@users.route('/account/<username>', methods=['GET', 'POST'])
def account(username):
    """
    Account page that displays username, user avatar, a count of user recipes,
    user password change, and list user recipe cards if they exist, else
    add recipe button.
    """

    # Finds username in collection based on session username

    username = coll_users.find_one({'username': session['username'
                                   ]})['username']

    # Finds user id in collection based on id of session user

    user_id = coll_users.find_one({'username': session['username'
                                  ]})['_id']

    # Finds avatar based on username

    user_avatar = coll_users.find_one({'username': session['username'
            ]})['user_avatar']

    # Finds user recipes based on author id and sorts by recipe name

    user_recipes = \
        coll_recipes.find({'author': user_id}).sort([('recipe_name',
            1)])

    # Gets count of user recipes

    count = coll_recipes.find({'author': user_id}).count()
    return render_template(
        'account.html',
        username=username,
        user_avatar=user_avatar,
        user_recipes=user_recipes,
        count=count,
        title='My Account',
        )


# ----- UPDATE PASSWORD ----- #

@users.route('/edit/<username>/', methods=['GET', 'POST'])
def update_password(username):
    """
    Change password functions allows user to update password.
    The Password form is called from users/form.py.
    User must enter current password, then enter and
    confirm new password.
    """

    # Finds username in collection based on session username

    username = coll_users.find_one({'username': session['username'
                                   ]})['username']

    # Defines form as PasswordForm from users/form.py

    form = PasswordForm()

    if form.validate_on_submit():

        # Passes username variable to form

        form = PasswordForm(username)

        # If current password field matches existing password in collection

        if check_password_hash(coll_users.find_one({'username': username})['pass'
                               ], request.form.get('current_password')):

            # User entry in collection is updated with new password

            coll_users.update_one({'username': username},
                                  {'$set': {'pass': generate_password_hash(request.form.get('new_password'
                                  ))}})
            return redirect(url_for('users.account', username=username))
        else:

            flash('Original password is incorrect!')
            return redirect(url_for('users.update_password',
                            username=username))

    return render_template('change_password.html', username=username,
                           form=form, title='Change Password')


# ----- LOGOUT ----- #
# Ends session and redirects to homepage

@users.route('/logout')
def logout():
    """
   Logout function log user out and redirects to homepage.
    """

    # Ends session

    session.clear()
    return redirect(url_for('main.home'))
