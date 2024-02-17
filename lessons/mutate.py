"""Mutating functions."""


__author__: str = "730718367"


def manual_append(x: list[int], y: int) -> None: 
    """Manually append."""
    x.append(y)
    return


a: list[int] = [1, 2, 3]
manual_append(a, 2)
print(a)


def double(x: list[int]) -> None: 
    """Double every element."""
    x_idx: int = 0
    while x_idx < len(x):
        x[x_idx] = x[x_idx] * 2
        x_idx += 1
    return


b: list[int] = [1, 2, 3]
double(b)
print(b)