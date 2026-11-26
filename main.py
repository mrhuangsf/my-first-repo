import sys
from datetime import datetime


def greet(name):
    return f"Hello, {name}! Welcome to GitHub."


def farewell(name):
    return f"Goodbye, {name}! See you next time."


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(greet(name))
    print(farewell(name))
    print(f"Today is {datetime.now():%Y-%m-%d}.")
