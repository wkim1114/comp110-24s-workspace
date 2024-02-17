
# Function name: display
# Parameter: list[str]
# Return nothing!
# Print out the list!

list_1: list[str] = ["c", "o", "m", "p"]

idx_list: int = 0
if idx_list <= len(list_1):
    print(list_1[idx_list])
    idx_list += 1

#def display(word: list[str]) -> None:
#    print(word)

#display
#x = display("Alyssa", "Erin", "AJ")
#print(x)

# Create a list
# Name: create
# Parameters: str and str
# Return list[str]
# Put both parameters into a list

def create(x: str, y: str) -> list[str]:
    list_create: list[str] = [x, y]
    return list_create

print(create(input(), input()))

def create(word1: str, word2: str) -> list[str]:
    my_list: list[str] = [word1, word2]
    return my_list

create("Hello", "world")

x: list[str] = create("Hello", "world")