from flask import Flask, render_template, url_for, flash, redirect, request, session
from whisk import app, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from whisk.forms import LoginForm, RegistrationForm
from bson.objectid import ObjectId

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
#User registration function
def register():
    # Check is user already logged in
    if 'logged_in' in session:  
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():

        user = mongo.db.user
        dup_user = user.find_one({'username': request.form['username'].title()})

        if dup_user is None:
            hash_pass = generate_password_hash(request.form['password'])
            user.insert_one({'username': request.form['username'].title(),
                             'pass': hash_pass})
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
    # Check if already logged in
    if 'logged_in' in session:  
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.user
        existing_user = user.find_one({
                                'username': request.form['username'].title()})
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

@app.route('/account/')
# User account page after login
def account(user_id):
    return render_template('account.html', title='Account')

@app.route('/logout')
# Ends session and redirects to homepage
def logout():
    # Ends session
    session.clear()  
    return redirect(url_for('home'))