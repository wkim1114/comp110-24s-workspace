"""Modifying lists with functions."""

def emphasize_str(word: str):
    word += "!"


a: str = "Hello"
emphasize_str(a)
print(a)


def emphasize_lists(word: list[str]):
    word.append("!")


b: list[str] = ["H", "E", "L", "L", "O"]
emphasize_lists(b)
print(b)