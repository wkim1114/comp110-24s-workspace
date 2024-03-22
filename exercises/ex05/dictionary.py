"""EX05 - Dictionary Functions."""

__author__ = "730718367"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert keys and values within a dictionary."""
    output_dict: dict[str, str] = {}
    
    """Empty dict check."""
    if len(input_dict) == 0:
        return output_dict
    
    """Key check."""
    test_list: list[str] = []
    for key in input_dict:
        test_list.append(input_dict[key])
    key_check: str = test_list[0]
    idx: int = 1
    while idx < len(test_list):
        if key_check is test_list[idx]:
            raise KeyError("Same value in dictionary.")
        idx += 1
    
    """Inverting."""
    for key in input_dict:
        output_dict[input_dict[key]] = key
    return output_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Empty dict check."""
    if len(input_dict) == 0:
        return ""
    
    """Find favorite color in the group."""
    counting_dict: dict[str, int] = {}
    for name in input_dict:
        if input_dict[name] not in counting_dict:
            counting_dict[input_dict[name]] = 1
        if input_dict[name] in counting_dict:
            counting_dict[input_dict[name]] += 1
    
    """Finding favorite color"""
    highest_vote: int = 0
    favorite_color_choice: str = ""
    for color in counting_dict:
        if counting_dict[color] > highest_vote:
            highest_vote = counting_dict[color]
            favorite_color_choice = color
    return favorite_color_choice


def count(input_list: list[str]) -> dict[str, int]:
    """Count the elements in the list and put them into counted dict[str, int]."""
    output_dict: dict[str, int] = {}
    
    """Empty dict check."""
    if len(input_list) == 0:
        return output_dict

    """Counting."""
    for elem in input_list:
        if elem not in output_dict:
            output_dict[elem] = 1
        else:
            output_dict[elem] += 1
    return output_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Alphabetize list into dictionary."""
    output_dict: dict[str, list[str]] = {}
    
    """Empty list check."""
    if len(input_list) == 0:
        return output_dict
    
    """Alphabetize."""
    for elem in input_list:
        if elem[0].lower() in output_dict:
            output_dict[elem[0].lower()] += [elem]        
        else:
            output_dict[elem[0].lower()] = [elem]
    return output_dict


def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Update attendance."""
    if day not in input_dict:
        input_dict[day] = []
    for key in input_dict:
        if key is day:
            if student in input_dict[key]:
                return None
            else:
                input_dict[key].append(student)
    return None