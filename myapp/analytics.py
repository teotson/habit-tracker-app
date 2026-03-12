from datetime import datetime, timedelta

def compute_longest_streak_for_habit(habit):
    if not habit.completions:
        return 0

    dates = sorted({datetime.fromisoformat(d).date() for d in habit.completions})

    if habit.periodicity == "daily":
        longest = cur = 1
        for i in range(1, len(dates)):
            if dates[i] == dates[i-1] + timedelta(days=1):
                cur += 1
            else:
                cur = 1
            longest = max(longest, cur)
        return longest

    elif habit.periodicity == "weekly":
        weeks = sorted({(d.isocalendar()[0], d.isocalendar()[1]) for d in dates})
        longest = cur = 1
        for i in range(1, len(weeks)):
            y0, w0 = weeks[i-1]
            y1, w1 = weeks[i]
            if (y1 * 53 + w1) == (y0 * 53 + w0) + 1:
                cur += 1
            else:
                cur = 1
            longest = max(longest, cur)
        return longest

    else:
        raise ValueError("Unsupported periodicity")
