# flask-user-login
A simple login form for any Flask application responsible for logging users in and out

This is a side project that I am working on as I learn how to build web applications with [Flask](http://flask.pocoo.org/). Its purpose is to provide a simple way to log users in and out of any systems. There are many ways to do that with Flask and there are many packages that can be used in order to provide such functionality. This project tries to use the simplest method to log users in and out of the application and it will be updated as I learn more about how to build apps with Flask.

The packages that are used are:

1.  [flask](http://flask.pocoo.org/)
2.  [flask-login](https://flask-login.readthedocs.org/en/latest/)
3.  [flask-sqlalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)
4.  psycopg (if PostgreSQL is used as a Database Management System)


---
To use the package you need to do the following steps:
1. From the `config-example.py` file create the `config.py` file with:
```
  cp config-example.py config.py
```
2. Modify the `config.py` file to include your database URI. See [this for more information](http://flask-sqlalchemy.pocoo.org/2.1/config/#connection-uri-format)
3. Install your virtual environment and then activate it. More info [here](http://flask.pocoo.org/docs/0.10/installation/)
4. Install the package dependencies by running the `setup.sh` script.

---
This is an infant project created to help me explore Flask's capabilities, but it might be useful to someone else aswell.
