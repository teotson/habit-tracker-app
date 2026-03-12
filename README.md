# Habit Tracking Application

## Project Overview
This project is a simple Habit Tracking Application developed in Python. 
It allows users to track daily and weekly habits and analyse their longest streaks.

## Features
- Create and track habits
- Support for daily and weekly habits
- Store habit data using JSON
- Analyse longest streaks
- Command Line Interface (CLI)
- Automated tests with pytest

## Project Structure
- `myapp/` – main application code
- `fixtures/` – predefined habit data
- `tests/` – unit tests

## Installation
Install the required dependencies:

pip install -r requirements.txt

## Run the application

python -m myapp.cli

To compute the longest streaks:

python -m myapp.cli longest_streaks

## Run tests

python -m pytest

## Author
Teodora Dimitrova Tsoncheva  
Student ID: 9210487
