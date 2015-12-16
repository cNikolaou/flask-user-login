from flask import Flask, render_template, request, flash, redirect
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.login import LoginManager
import config

# Configuration
SECRET_KEY = "secret!"
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

## App initiallization
app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
#login_manager = LoginManager()
#login_manager.init_app(app)


## Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


## Views
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":

        username = request.form['username']
        password = request.form['password']

        flash('Username:%s and password:%s' % (username, password))

        user = User.query.filter_by(username=username).first()

        if user is None:
            flash('Username does not exist in the database')
            return redirect('/login')
        else:
            if password != user.password:
                flash('WRONG PASSWORD!')
                return redirect('/login')
            else:
                flash('Logged into the system!')
                flash('Hello %s' % username)
                return redirect('/login')

        #flash('User not found!')
        return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/create_account', methods=['GET', 'POST'])
def create_account():

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
            return redirect('/create_account')


        # Check if the passwords do not match
        if password != test_password:
            flash('Passwords do not match')
            return redirect('/create_account')
        elif not password:
            flash('Please enter a password for your account.')
            return redirect('/create_account')

        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created. You can now log into the system.')
        return redirect('/login')

    return render_template('create_account.html')


if __name__ == '__main__':
    app.run(debug=True)
