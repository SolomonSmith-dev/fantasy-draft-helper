# __init__.py
# This file initializes Flask application and makes it available to other parts of the project.

from flask import Flask

#Create an instance of the Flask class
# The first argument is the name of the application’s module or package.
app = Flask(__name__)

# Import routes so they are registered with the app
# This is where you define the routes for your application.
from app import routes
