"""EX03 - Functional Battleship."""


__author__ = "730718367"


import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid_size: int, ______: str) -> int: 
    """Input guess function."""
    row_size: int = grid_size
    column_size: int = grid_size
    assert ______ == "row" or ______ == "column"
    
    if ______ == "row":
        row_guess = int(input("Guess a row: "))
        while row_guess > row_size or row_guess < 1:
            row_guess = int(input(f"The grid is only {row_size} by {column_size}. Try again: "))
        return row_guess
    
    else:
        column_guess = int(input("Guess a column: "))
        while column_guess > column_size or column_guess < 1:
            column_guess = int(input(f"The grid is only {row_size} by {column_size}. Try again: "))
        return column_guess


def print_grid(grid_size: int, row_guess: int, column_guess: int, correct: bool) -> None:
    """Print grid function."""
    row_size: int = grid_size

    BLANK = str(BLUE_BOX * int(row_size))
    HIT = str(BLUE_BOX * (column_guess - 1) + RED_BOX + BLUE_BOX * (int(row_size) - column_guess))
    MISS = str(BLUE_BOX * (column_guess - 1) + WHITE_BOX + BLUE_BOX * (int(row_size) - column_guess))

    row_counter: int = 0

    while row_counter < row_size:
        row_counter += 1 
        if row_guess == row_counter: 
            if correct is True:
                print(HIT)
            else:
                print(MISS)
        else: 
            print(BLANK)


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool: 
    """Correct guess function."""
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False
    

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Main game function."""
    game_idx: int = 0
    while game_idx < 5:
        game_idx += 1
        print(f"=== Turn {game_idx}/5 ===")
        
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
        correct: bool = correct_guess(secret_row, secret_column, row_guess, column_guess)
        
        if correct is True:
            print_grid(grid_size, row_guess, column_guess, correct)
            print("Hit!")
            print(f"You won in {game_idx}/5 turns!")
            return
        else:
            print_grid(grid_size, row_guess, column_guess, correct)
            print("Miss!")
    print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))