import json
from datetime import datetime

def load_input_json(path="C:\\Users\\Admin\\Desktop\\Adobe\\Adobe25-1b\\input\\input.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    filenames = [d["filename"] for d in data["documents"]]
    return data["challenge_info"], data["persona"]["role"], data["job_to_be_done"]["task"], filenames

def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def timestamp():
    return datetime.now().isoformat()
