"""EX02 - One Shot Battleship."""

__author__ = "730718367"

#emoji bin
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


#row/column size & secret row/column
row_size = int(4)
column_size = int(4)
secret_row = int(3)
secret_column = int(2)


#output string bin
BLANK = str(BLUE_BOX * int(row_size))

HIT_1 = str(BLUE_BOX * (1-1) + RED_BOX + BLUE_BOX * (int(row_size)-1))
HIT_2 = str(BLUE_BOX * (2-1) + RED_BOX + BLUE_BOX * (int(row_size)-2))
HIT_3 = str(BLUE_BOX * (3-1) + RED_BOX + BLUE_BOX * (int(row_size)-3))
HIT_4 = str(BLUE_BOX * (4-1) + RED_BOX + BLUE_BOX * (int(row_size)-4))

MISS_1 = str(BLUE_BOX * (1-1) + WHITE_BOX + BLUE_BOX * (int(row_size)-1))
MISS_2 = str(BLUE_BOX * (2-1) + WHITE_BOX + BLUE_BOX * (int(row_size)-2))
MISS_3 = str(BLUE_BOX * (3-1) + WHITE_BOX + BLUE_BOX * (int(row_size)-3))
MISS_4 = str(BLUE_BOX * (4-1) + WHITE_BOX + BLUE_BOX * (int(row_size)-4))


#using while loop to only accept valid inputs
row_guess = int(input("Guess a row: "))
while row_guess > row_size:
    row_guess = int(input(f"The grid is only {row_size} by {column_size}. Try again: "))

column_guess = int(input("Guess a column: "))
while column_guess > column_size:
    column_guess = int(input(f"The grid is only {row_size} by {column_size}. Try again: "))


#while loop to create stacks of strings
row_counter = int(0)

while row_counter < row_size:
    row_counter += 1 #staking counter
    if row_guess == row_counter: #output string prints only when input row matches stacking counter
        if column_guess == secret_column and row_guess == secret_row: #Both row and column must be equal to secret to print HIT strings
            if column_guess == 1:
                print(HIT_1)
            elif column_guess == 2:
                print(HIT_2)
            elif column_guess == 3:
                print(HIT_3)
            elif column_guess == 4:
                print(HIT_4)
        else: #else print MISS strings
            if column_guess == 1:
                print(MISS_1)
            elif column_guess == 2:
                print(MISS_2)
            elif column_guess == 3:
                print(MISS_3)
            elif column_guess == 4:
                print(MISS_4)
    else:
        print(BLANK) #stacking BLANK strings to make row by column size output


#hit or miss printer
if row_guess == secret_row and column_guess == secret_column: #both correct, hit
    print("Hit!")
elif row_guess == secret_row and column_guess != secret_column: #row correct / column incorrect, close + hint
    print("Close! Correct row, wrong column.")
elif row_guess != secret_row and column_guess == secret_column: #row incorrect / column correct, close + hint
    print("Close! Correct column, wrong row.")
else: #else, miss
    print("Miss!")
