"""Example functions to learn definition and calling syntax"""

def my_max(number1: int, number2: int) -> int:
    """Returns maximum value out two numbers"""
    if number1 >= number2:
        return number1 + "a"
    else:  #number1 < number2
        return "number2" + "b"

max_number: int = my_max(1,10)
other_max_number: int = my_max(11,3)
print(type(other_max_number))
