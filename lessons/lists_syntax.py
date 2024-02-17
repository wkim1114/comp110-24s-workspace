"""Demonstrate Basic List Syntax"""

# Initialize an empty list
grocery_list: list[str] = list() # <- list constructor
grocery_list: list[str] = [] # <- literal

print(grocery_list)

# Add item to a list
grocery_list.append("banana")
grocery_list.append("milk")
grocery_list.append("bread")

print("After appending: ")
print(grocery_list)

# Create an already populated list
grocery_list2: list[str] = ["banana", "milk", "bread"]

print("Populated list: ")
print(grocery_list2)

grocery_list2.append("egg")

print(grocery_list2)

# Indexing
print("Print first element of string: ")
print(grocery_list2[0])

# Modifying by Index
print("Before change: ")
print(grocery_list2)

grocery_list2[0] = "almond milk"

print("After change: ")
print(grocery_list2)

# Not valid for strings
# x: str = "cats"
# x[2] = "r"

# Length of a list
print(len(grocery_list))
print(len(grocery_list2))

# Remove an item from a list
print("Before change: ")
print(grocery_list2)

grocery_list2.pop(0)

print("After change: ")
print(grocery_list2)

print(grocery_list[10])