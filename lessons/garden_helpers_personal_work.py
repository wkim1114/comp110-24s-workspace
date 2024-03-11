"""Some functions for my garden plan!"""

__author__ = "730718367"

by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
by_date: dict[str, list[str]] = {"April": ["marigold"], "June":["carrots"]}

new_plant: str = "daisy"
new_plant_kind: str = "flower"

new_fruit: str = "elderberry"
new_fruit_kind: str = "fruit"

# want to get: {"flower"; ["marigold", "zinnia", "daisy"], "vegetable": ["carrots"]}

print(by_kind)

def add_by_kind(input_dict = dict[str, list[str]], kind = str, plant = str) -> None:
    """Add on to dictionary kind and plant."""
    empty_list: list[str] = []
    if kind not in input_dict:
        input_dict[kind] = empty_list
    for idx in input_dict:
        if kind is idx:
            input_dict[idx].append(plant)
    return

add_by_kind(by_kind, new_plant_kind, new_plant)

print(by_kind)

add_by_kind(by_kind, new_fruit_kind, new_fruit)

print(by_kind)
