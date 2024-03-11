"""Splitting a dictionary into two lists."""


__author__ = "730718367"


def get_keys(x: dict[str, int]) -> list[str]: 
    """Get keys."""
    y: list[str] = []
    if len(x) == 0:
        return y
    for key in x: 
        y.append(key)
    print(y)
    return y


def get_values(x: dict[str, int]) -> list[int]: 
    """Get values."""
    y: list[int] = []
    if len(x) == 0:
        return y
    for key in x: 
        y.append(x[key])
    print(y)
    return y


test: dict[str, int] = {"Hello": 1, "World": 2}

get_keys(test)

get_values(test)