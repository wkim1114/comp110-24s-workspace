"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730718367"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

Secret_Boat_Location = int(input("Pick a secret boat location between 1 and 4: "))

if Secret_Boat_Location < 1:
    print(f"Error! {Secret_Boat_Location} too low!")
    exit()
elif Secret_Boat_Location > 4:
    print(f"Error! {Secret_Boat_Location} too high!")
    exit()

Guess = int(input("Guess a number between 1 and 4: "))

if Guess < 1:
    print(f"Error! {Guess} too low!")
    exit()
elif Guess > 4:
    print(f"Error! {Guess} too high!")
    exit()


if Guess == 1:
    if Secret_Boat_Location == Guess:
        print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
        print("Correct! You hit the ship.")
    else:
        print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
        print("Incorrect! You missed the ship.")
elif Guess == 2:
    if Secret_Boat_Location == Guess:
        print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
        print("Correct! You hit the ship.")
    else:
        print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
        print("Incorrect! You missed the ship.")
elif Guess == 3:
    if Secret_Boat_Location == Guess:
        print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
        print("Correct! You hit the ship.")
    else:
        print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
        print("Incorrect! You missed the ship.")
else:
    if Secret_Boat_Location == Guess:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
        print("Correct! You hit the ship.")
    else:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)
        print("Incorrect! You missed the ship.")