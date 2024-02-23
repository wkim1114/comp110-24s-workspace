"""EX04 - list Utility Functions."""


__author__ = "730718367"


def all(x: list[int], y: int) -> bool:
    """Check if all elements of x are equal to integer y."""
    idx: int = 0
    if len(x) == 0:
        print("False")
        return False
    while len(x) > idx:
        if x[idx] != y:
            print("False")
            return False
        idx += 1
    print("True")
    return True


all([1, 2, 3], 1)

all([1, 1, 1], 2)

all([1, 1, 1], 1)

all([], 1)


def max(x: list[int]) -> int:
    """Find the maximum element of list x."""
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    max_val: int = x[idx]
    while len(x) > idx:
        if x[idx] > max_val:
            max_val = x[idx]
        idx += 1
    print(max_val)
    return max_val


max([1, 3, 2])

max([100, 99, 98])


def is_equal(x: list[int], y: list[int]) -> bool:
    """Find if two lists are equal to each other."""
    idx: int = 0
    if len(x) == len(y):
        while len(x) > idx:
            if x[idx] != y[idx]:
                print("False")
                return False
            else:
                idx += 1
        print("True")
        return True
    else:
        print("False")
        return False


is_equal([1, 0, 1], [1, 0, 1])

is_equal([1, 0, 1], [1, 0, 0])

is_equal([1, 0], [1, 0, 0])


def extend(x: list[int], y: list[int]) -> None:
    """Extend the list x by adding elements of list y."""
    idx: int = 0
    while len(y) > idx:
        x.append(y[idx])
        idx += 1
    return


a: list[int] = [1, 3, 5]
b: list[int] = [2, 4, 6]
extend(a, b)
print(a)

c: list[int] = [7, 8]
extend(c, b)
print(c)