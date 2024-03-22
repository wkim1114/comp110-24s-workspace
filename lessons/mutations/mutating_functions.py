"""Functions that either mutate a list or don't."""


def remove_fist(input_list: list[str]) -> None:
    """Remove first element of imput_list. Mutating!"""
    input_list.pop(0)


def get_first(input_list: list[str]) -> str:
    """Return first element of input_list without mutating."""
    return input_list[0]


def get_and_remove_first(input_list: list[str]) -> str:
    """Return first element AND remove it."""
    elem: str = input_list[0]
    input_list.pop(0)
    return elem
