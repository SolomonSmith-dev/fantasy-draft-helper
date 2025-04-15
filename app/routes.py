# routes.py
# This file holds all the URL routes (endpoints) for Flask web app.

from app import app
from flask import render_template  # Used to render HTML files
import pandas as pd  # Pandas is used to read and handle CSV data
from app.draft_logic import build_draft_pool, draft_best_player, init_team, add_to_team

# routes.py
# This file holds all the URL routes (endpoints) for Flask web app.
# The main route for the web application 
@app.route("/")
def index():
    df = pd.read_csv("data/players.csv")
    players = df.to_dict(orient="records")
    
    # Draft logic test
    draft_pool = build_draft_pool(players)
    my_team = init_team()

    # Simulate 3 draft picks
    for _ in range(3):
        pick = draft_best_player(draft_pool)
        if pick:
            add_to_team(my_team, pick)
#           players.remove(pick)  # Remove from available players
    return render_template("index.html", players=players, team=my_team)