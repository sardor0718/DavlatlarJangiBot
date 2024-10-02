import json
import os

DATA_DIR = "user_data"

def load_user_data(user_id):
    user_file = os.path.join(DATA_DIR, f"{user_id}.json")
    if os.path.exists(user_file):
        with open(user_file, "r") as f:
            return json.load(f)
    return {}

def save_user_data(user_id, user_data):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    user_file = os.path.join(DATA_DIR, f"{user_id}.json")
    with open(user_file, "w") as f:
        json.dump(user_data, f)
