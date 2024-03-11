"""EX05 - Dictionary Functions."""


__author__ = "730718367"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverst keys and values in a dictionary."""
    """Key check"""
    test_list: list[str] = []
    for key in input_dict:
        test_list.append(input_dict[key])
    key_check: str = test_list[0]
    idx: int = 1
    while idx < len(test_list):
        if key_check == test_list[idx]:
            raise KeyError("Same value in dictionary.")
        idx += 1
    
    """Inverting"""
    output_dict: dict[str, str] = {}
    for key in input_dict:
        output_dict[input_dict[key]] = key
    print(output_dict)
    return(output_dict)


def favorite_color(input_dict: dict[str, str]) -> str:
    """Find favorite color in the group."""
    """Listing colors"""
    color_list: list[str] = []
    for key in input_dict: 
        color_list.append(input_dict[key])
    
    """Counting colors"""
    color_dict: dict[str, int] = {}
    idx: int = 0
    while idx < len(color_list):
        if color_list[idx] in color_dict:
            color_dict[color_list[idx]] += 1
        else:
            color_dict[color_list[idx]] = 1
        idx += 1
    
    """Favorite color"""
    highest_number: int = 0
    for key in color_dict:
        if color_dict[key] > highest_number:
            highest_number = color_dict[key]
    favorite_color: str = ""
    for key in color_dict:
        if color_dict[key] is highest_number:
            favorite_color = key
    return favorite_color


def count(input_list: list[str]) -> dict[str, int]:
    """Count."""
    output_dict: dict[str, int] = {}
    for elem in input_list:
        if input_list[elem] in output_dict:
            output_dict[input_list[elem]] += 1
        else:
            output_dict[input_list[elem]] = 1
    return output_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Alphabetize list into dictionary."""
    output_dict: dict[str, list[str]] = {}
    for elem in input_list:
        if elem[0].lower() in output_dict:
            output_dict[elem[0].lower()] += [elem]        
        else:
            output_dict[elem[0].lower()] = [elem]
    return output_dict


def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Update attendance."""
    if day not in input_dict:
        input_dict[day] = []
    for key in input_dict:
        if key is day:
            input_dict[key] += [student]
    return input_dict