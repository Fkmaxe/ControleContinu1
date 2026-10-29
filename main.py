STRAIGHT_FLUSH_VALUE = 80
FOUR_OF_A_KIND_VALUE = 60
FULL_HOUSE_VALUE = 50
FLUSH_VALUE = 45
STRAIGHT_VALUE = 40
THREE_OF_A_KIND_VALUE = 30


def value_hand(hand: list) -> int:
    if is_straight_flush(hand):
        return STRAIGHT_FLUSH_VALUE
    if is_four_of_a_kind(hand):
        return FOUR_OF_A_KIND_VALUE
    if is_full_house(hand):
        return FULL_HOUSE_VALUE
    if is_flush(hand):
        return FLUSH_VALUE
    if is_straight(hand):
        return STRAIGHT_VALUE
    if is_three_of_a_kind(hand):
        return THREE_OF_A_KIND_VALUE
    return highest_card_value(hand)


def sorted_values(hand: list) -> list:
    return sorted(card[1] for card in hand)


def is_straight_flush(hand: list) -> bool:
    return is_flush(hand) and is_straight(hand)


def is_four_of_a_kind(hand: list) -> bool:
    values = sorted_values(hand)
    return values[0] == values[3] or values[1] == values[4]


def is_full_house(hand: list) -> bool:
    return len(set(sorted_values(hand))) == 2


def is_flush(hand: list) -> bool:
    first_suit = hand[0][0]
    return all(card[0] == first_suit for card in hand)


def is_straight(hand: list) -> bool:
    values = sorted_values(hand)
    lowest = values[0]
    return values == list(range(lowest, lowest + 5))


def is_three_of_a_kind(hand: list) -> bool:
    return hand[0][1] == hand[1][1] == hand[2][1]


def highest_card_value(hand: list) -> int:
    return max(card[1] for card in hand)
