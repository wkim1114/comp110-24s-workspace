"""EX02 - One Shot Battleship."""

__author__ = "730718367"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


row_size = int(4)
column_size = int(4)
secret_row = int(3)
secret_column = int(2)


BLANK = str(BLUE_BOX * int(row_size))

HIT_1 = str(BLUE_BOX * (1-1) + RED_BOX + BLUE_BOX * (int(row_size)-1))
HIT_2 = str(BLUE_BOX * (2-1) + RED_BOX + BLUE_BOX * (int(row_size)-2))
HIT_3 = str(BLUE_BOX * (3-1) + RED_BOX + BLUE_BOX * (int(row_size)-3))
HIT_4 = str(BLUE_BOX * (4-1) + RED_BOX + BLUE_BOX * (int(row_size)-4))

MISS_1 = str(BLUE_BOX * (1-1) + WHITE_BOX + BLUE_BOX * (int(row_size)-1))
MISS_2 = str(BLUE_BOX * (2-1) + WHITE_BOX + BLUE_BOX * (int(row_size)-2))
MISS_3 = str(BLUE_BOX * (3-1) + WHITE_BOX + BLUE_BOX * (int(row_size)-3))
MISS_4 = str(BLUE_BOX * (4-1) + WHITE_BOX + BLUE_BOX * (int(row_size)-4))


row_guess = int(input("Guess a row: "))
while row_guess > row_size or row_guess < 1:
    row_guess = int(input(f"The grid is only {row_size} by {column_size}. Try again: "))

column_guess = int(input("Guess a column: "))
while column_guess > column_size or column_guess < 1:
    column_guess = int(input(f"The grid is only {row_size} by {column_size}. Try again: "))


row_counter = int(0)

while row_counter < row_size:
    row_counter += 1 
    if row_guess == row_counter: 
        if column_guess == secret_column and row_guess == secret_row:
            if column_guess == 1:
                print(HIT_1)
            elif column_guess == 2:
                print(HIT_2)
            elif column_guess == 3:
                print(HIT_3)
            elif column_guess == 4:
                print(HIT_4)
        else: 
            if column_guess == 1:
                print(MISS_1)
            elif column_guess == 2:
                print(MISS_2)
            elif column_guess == 3:
                print(MISS_3)
            elif column_guess == 4:
                print(MISS_4)
    else:
        print(BLANK)


if row_guess == secret_row and column_guess == secret_column:
    print("Hit!")
elif row_guess == secret_row and column_guess != secret_column:
    print("Close! Correct row, wrong column.")
elif row_guess != secret_row and column_guess == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")
