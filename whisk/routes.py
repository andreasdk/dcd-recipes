from flask import Flask, render_template, url_for, flash, redirect, request, session
from whisk import app
from werkzeug.security import generate_password_hash, check_password_hash
from whisk.forms import LoginForm, RegistrationForm

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
        dup_user = user.find_one({'name': request.form['username'].title()})

        if dup_user is None:
            hash_pass = generate_password_hash(request.form['password'])
            user.insert_one({'name': request.form['username'].title(),
                             'pass': hash_pass})
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect(url_for('home'))

        flash('Sorry, username already taken. Please try another.')
        return redirect(url_for('register'))
    return render_template('register.html', form=form, title="Register")


@app.route('/login', methods=['GET', 'POST'])
#User login function
def login():
    # Check is already logged in
    if 'logged_in' in session:  
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.user
        logged_in_user = user.find_one({
                                'name': request.form['username'].title()})

        if logged_in_user:
            if check_password_hash(logged_in_user['pass'],
                                   request.form['password']):
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('home'))
            flash('Sorry incorrect password!')
            return redirect(url_for('login'))
    return render_template('login.html', form=form, title='Login')

@app.route('/logout')
# Ends session and redirects to homepage
def logout():
    # Ends session
    session.clear()  
    return redirect(url_for('home'))