import os

HISTORY_FILE = "history.txt"


def add_to_history(name1: str, name2: str, percentage: int, message: str):
    """
    Add a new result to the history list and also save it to a file.
    """
    entry = f"{name1.title()} & {name2.title()} → {percentage}% | {message}"

    # Save to file
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")


def get_history() -> list[str]:
    """
    Return all previous results as a list of strings.
    """
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Clean the lines
    history = [line.strip() for line in lines if line.strip()]
    return history


def clear_history():
    """
    Clear the history file.
    """
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
