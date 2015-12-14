from flask import Flask, render_template, request
from flask.ext.login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    return render_template('create_account.html')


if __name__ == '__main__':
    app.run(debug=True)
