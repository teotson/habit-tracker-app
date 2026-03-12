from datetime import datetime

class Habit:
    def __init__(self, name, periodicity, id=None):
        self.id = id or name.lower().replace(" ", "_")
        self.name = name
        self.periodicity = periodicity
        self.completions = []

    def add_completion(self, iso_datetime_str):
        dt = datetime.fromisoformat(iso_datetime_str)
        self.completions.append(dt.isoformat())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "periodicity": self.periodicity,
            "completions": self.completions
        }

    @staticmethod
    def from_dict(d):
        h = Habit(d["name"], d.get("periodicity", "daily"), id=d.get("id"))
        h.completions = d.get("completions", [])
        return h
