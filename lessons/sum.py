"""Summing the elements of a list using different loops."""


__author__ = "730718367"


def w_sum(vals: list[float]) -> float:
    """Utilizes while idx."""
    if len(vals) == 0:
        print(0.0)
        return 0.0
    idx: int = 0
    result: float = 0.0
    while idx < len(vals):
        result += vals[idx]
        idx += 1
    print(result)
    return result


w_sum([1.1, 0.9, 1.0])

w_sum([])


def f_sum(vals: list[float]) -> float:
    """Utilizes for...in..."""
    result: float = 0.0
    for elem in vals:
        result += elem
    print(result)
    return result


f_sum([1.1, 0.9, 1.0])

f_sum([])


def f_range_sum(vals: list[float]) -> float:
    """Utilizing for...in...range..."""
    result: float = 0.0
    for idx in range(0, len(vals)):
        result += vals[idx]
    print(result)
    return result


f_range_sum([1.1, 0.9, 1.0])

f_range_sum([])