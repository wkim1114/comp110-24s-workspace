"""Practice with variables and input function"""

name: str = input("What is your name?")
number_str: str = input("What is your PID?")
number: int = int(number_str)
higher_number: int = number + 1

print("Hello, " + name + "!")
print("Your PID is " + str(number))
