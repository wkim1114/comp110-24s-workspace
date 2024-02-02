"""Practice while loops and debug them"""

my_number: int = int(8675309)
my_number_str: str = str(my_number)
total: int = int(0)
index: int = int(0)
while index < len(my_number_str):
    value: int = int(my_number_str[index])
    total += value
    index += 1