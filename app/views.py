from flask import render_template, url_for, redirect, flash, request
from flask.ext.login import login_user, logout_user, login_required
from app import app, db, login_manager
from models import User


## Views
@app.route('/')
@app.route('/index')
def index():
    '''
    Main function called when accessing the website.
    '''

    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    A function that handles the login functionality. This is a really simple
    form of the function. WTForms and Flask-WTF can be used to improve the
    function.
    '''

    if request.method == "POST":

        username = request.form['username']
        password = request.form['password']

        flash('Username:%s and password:%s' % (username, password))

        user = User.query.filter_by(username=username).first()

        # Check if the given username exists in the database and whether the
        # given password matches the one that was given when creating the
        # account.
        if user is None:
            flash('Username does not exist in the database')
            return redirect(url_for('login'))
        else:
            if password != user.password:
                flash('WRONG PASSWORD!')
                return redirect(url_for('login'))
            else:
                login_user(user)
                flash('Logged into the system!')
                flash('Hello %s' % username)
                return redirect(url_for('index'))

        #flash('User not found!')
        return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    '''
    Handles the user creation and tests the edge cases when creating a new
    user.
    '''

    if request.method == "POST":

        # get the input values from the user
        username = request.form['username']
        password = request.form['password']
        test_password = request.form['test_password']

        flash('Username:%s and password:%s and test_password:%s'
                % (username, password, test_password))


        # Check if the username is already taken
        if User.query.filter_by(username=username).first() is not None :
            flash('Username already exists. Choose another username.')
            return redirect(url_for('create_account'))


        # Check if the passwords do not match
        if password != test_password:
            flash('Passwords do not match')
            return redirect(url_for('create_account'))
        elif not password:
            flash('Please enter a password for your account.')
            return redirect(url_for('create_account'))

        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created. You can now log into the system.')
        return redirect(url_for('login'))

    return render_template('create_account.html')



@app.route('/logout')
@login_required
def logout():
    '''
    Implements the basic logout functinality
    '''
    logout_user()
    flash('You were logged out!')
    return redirect(url_for('index'))



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
