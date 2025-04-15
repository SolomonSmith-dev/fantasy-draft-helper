# routes.py
# This file holds all the URL routes (endpoints) for Flask web app.

from app import app
from flask import render_template  # Used to render HTML files
import pandas as pd  # Pandas is used to read and handle CSV data

# Define a route for the home page
@app.route("/")
def index():
    # Load player data from a CSV file
    df = pd.read_csv("data/players.csv")
    
    # Convert DataFrame to a list of dictionaries so it can be easily used in the template
    players = df.to_dict(orient="records")

    # Render the HTML template and pass the player data to it
    return render_template("index.html", players=players)
