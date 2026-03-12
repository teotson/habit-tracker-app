from myapp.analytics import compute_longest_streak_for_habit
from myapp.habit import Habit

def test_longest_streak_daily():
    h = Habit("Exercise", "daily")
    h.completions = [
        "2025-09-11T08:00:00",
        "2025-09-12T08:00:00",
        "2025-09-13T08:00:00"
    ]
    assert compute_longest_streak_for_habit(h) == 3
