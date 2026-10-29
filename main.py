from collections import Counter, namedtuple

Card = namedtuple("Card", ["suit", "value"])

HEARTS = "Hearts"
DIAMONDS = "Diamonds"
CLUBS = "Clubs"
SPADES = "Spades"

STRAIGHT_FLUSH_POINTS = 80
FOUR_OF_A_KIND_POINTS = 60
FULL_HOUSE_POINTS = 50
FLUSH_POINTS = 45
STRAIGHT_POINTS = 40
THREE_OF_A_KIND_POINTS = 30


def total_points(hands: list) -> int:
    return sum(hand_points(hand) for hand in hands)


def hand_points(hand: list) -> int:
    if is_straight_flush(hand):
        return STRAIGHT_FLUSH_POINTS
    if is_four_of_a_kind(hand):
        return FOUR_OF_A_KIND_POINTS
    if is_full_house(hand):
        return FULL_HOUSE_POINTS
    if is_flush(hand):
        return FLUSH_POINTS
    if is_straight(hand):
        return STRAIGHT_POINTS
    if is_three_of_a_kind(hand):
        return THREE_OF_A_KIND_POINTS
    return highest_card_value(hand)


def sorted_values(hand: list) -> list:
    return sorted(card.value for card in hand)


def same_value_counts(hand: list) -> list:
    return sorted(Counter(card.value for card in hand).values())


def is_straight_flush(hand: list) -> bool:
    return is_flush(hand) and is_straight(hand)


def is_four_of_a_kind(hand: list) -> bool:
    return 4 in same_value_counts(hand)


def is_full_house(hand: list) -> bool:
    return same_value_counts(hand) == [2, 3]


def is_flush(hand: list) -> bool:
    suits = {card.suit for card in hand}
    return len(suits) == 1


def is_straight(hand: list) -> bool:
    values = sorted_values(hand)
    lowest = values[0]
    return values == list(range(lowest, lowest + 5))


def is_three_of_a_kind(hand: list) -> bool:
    return 3 in same_value_counts(hand)


def highest_card_value(hand: list) -> int:
    return max(card.value for card in hand)
