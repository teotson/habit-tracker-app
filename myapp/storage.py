import json
from myapp.habit import Habit

def save_to_file(habits, path):
    data = {"habits": [h.to_dict() for h in habits]}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_from_file(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Habit.from_dict(d) for d in data.get("habits", [])]
