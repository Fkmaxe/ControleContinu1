

def value_hand(hand: list):
    values: list = sorted(card[1] for card in hand)
    if all(card[0] == hand[0][0] for card in hand) and values == list(range(values[0], values[0] + 5)):
        return 80

    if values[0] == values[3] or values[1] == values[4]:
        return 60

    if len(set(values)) == 2:
        return 50

    if hand[0][1] == hand[1][1] == hand[2][1]:
        return 30

    if all(card[0] == hand[0][0] for card in hand):
        return 45

    if values == list(range(values[0], values[0] + 5)):
        return 40

    return max([card[1] for card in hand])

