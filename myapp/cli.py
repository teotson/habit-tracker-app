import click
from myapp.habit import Habit
from myapp.storage import save_to_file, load_from_file
from myapp.analytics import compute_longest_streak_for_habit
import os

DATAFILE = os.path.join(os.getcwd(), "fixtures", "5_habits_4weeks.json")

@click.group()
def cli():
    """Main command group for the Habit Tracker CLI."""
    pass

@cli.command(name="longest_streaks")
def longest_streaks():
    """Compute the longest streak for each habit."""
    habits = load_from_file(DATAFILE)
    for h in habits:
        s = compute_longest_streak_for_habit(h)
        click.echo(f"{h.name} ({h.periodicity}) → {s}")

if __name__ == "__main__":
    cli()
