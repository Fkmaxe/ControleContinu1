

def value_hand(hand: list):
    if hand[0][1] == hand[1][1] == hand[2][1]:
        return 30

    if all(card[0] == hand[0][0] for card in hand):
        return 50

    values = sorted(card[1] for card in hand)
    if values == list(range(values[0], values[0] + 5)):
        return 40

    return max([card[1] for card in hand])

