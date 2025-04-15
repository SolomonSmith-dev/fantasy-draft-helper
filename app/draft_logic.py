# draft_logic.py
# Core draft functions using real data structures

import heapq

# Load players and build a priority queue (min-heap) based on ADP
def build_draft_pool(players):
    """
    Build a min-heap (priority queue) based on ADP.
    Lower ADP = higher draft priority.
    """
    draft_pool = []
    for player in players:
        # Tuple format: (priority, player_data)
        heapq.heappush(draft_pool, (player['adp'], player))
    return draft_pool

# Initialize your fantasy team as a hash map by position
def init_team():
    """
    Initializes the player's team.
    Each position is a key in the dictionary.
    """
    return {
        "QB": [],
        "RB": [],
        "WR": [],
        "TE": [],
        "FLEX": [],
        "DEF": [],
        "K": []
    }

# Draft the best available player (lowest ADP)
def draft_best_player(draft_pool):
    """
    Removes and returns the best player (lowest ADP) from the pool.
    """
    if draft_pool:
        return heapq.heappop(draft_pool)[1]  # return only the player data
    return None

# Add player to your team hash map
def add_to_team(team, player):
    """
    Adds the drafted player to their position group on your team.
    """
    position = player['position']
    if position in team:
        team[position].append(player)
    elif position in ["RB", "WR", "TE"]:
        team["FLEX"].append(player)
    else:
        team["FLEX"].append(player)  # fallback
    return team
