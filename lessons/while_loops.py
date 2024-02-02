"""Demonstrate while loops by finding low values in string"""

cards: str = "5235"
card_idx: int = 0 #look at each number in the string
low_card: int = int(cards[0])

while card_idx < 4:
    print(cards[card_idx])
    card_idx = card_idx + 1

while card_idx < 4: #check if current card is less than low card
    current_card = int(cards[card_idx])
    if current_card < low_card: 
        low_card = current_card #update low card to be the value of current card
    card_idx = card_idx + 1
print(low_card)