

def value_hand(hand: list):
    values = sorted(card[1] for card in hand)
    if len(set(values)) == 2:
        return 60

    if hand[0][1] == hand[1][1] == hand[2][1]:
        return 30

    if all(card[0] == hand[0][0] for card in hand):
        return 50

    if values == list(range(values[0], values[0] + 5)):
        return 40

    return max([card[1] for card in hand])

