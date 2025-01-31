# lgts/validator.py
import re
from typing import List

class DAGValidationError(Exception):
    def __init__(self, errors: List[str]):
        self.errors = errors

def validate_dag(paths: List[List[str]]) -> None:
    passes = False
    errors = []
    start_state = "At(OutsideRoom)"
    goal_state = "At(Green_Goal)"
    key_pattern = re.compile(r"Holding\(Key\d+\)")
    door_pattern = re.compile(r"Unlocked\(Door\)")

    for idx, path in enumerate(paths):
        if not path:
            errors.append(f"Path {idx + 1} is empty.")
            continue
        if path[0] != start_state:
            errors.append(f"Path {idx + 1} does not start with {start_state}.")
        else:
            print(f"Path {idx + 1} starts with {start_state}. ")
        if path[-1] != goal_state:
            errors.append(f"Path {idx + 1} does not end with {goal_state}.")
        else:
            print(f"Path {idx + 1} ends with {goal_state}.")
        keys = sum(1 for state in path if key_pattern.match(state))
        doors = sum(1 for state in path if door_pattern.match(state))
        if doors > keys:
            errors.append(f"Path {idx + 1}: More doors unlocked than keys picked up.")
        else:
            print(f"Path {idx + 1}: Less or equal number of doors unlocked as there are keys picked up.")
    if errors:
        raise DAGValidationError(errors)
    passes = True
    if passes:
        print("\nPases all unit cases!\n")
