import pytest
from main import value_hand, value_hands

HIGH_CARD_HAND = [ ["Hearts" , 1], ["Diamonds" , 3],["Spades" , 5],["Clubs" , 7],["Hearts" , 14]]
THREE_OF_A_KIND_HAND = [ ["Hearts" , 1], ["Diamonds" , 1],["Spades" , 1],["Clubs" , 7],["Hearts" , 14]]
STRAIGHT_HAND = [ ["Hearts" , 4], ["Diamonds" , 2],["Spades" , 5],["Clubs" , 1],["Hearts" , 3]]
FLUSH_HAND = [ ["Hearts" , 4], ["Hearts" , 12],["Hearts" , 5],["Hearts" , 8],["Hearts" , 3]]
FULL_HAND = [ ["spades" , 4], ["Hearts" , 4],["Hearts" , 5],["spades" , 5],["clubs" , 5]]
FOUR_OF_A_KIND_HAND = [ ["Hearts" , 9], ["Diamonds" , 9],["Spades" , 9],["Clubs" , 9],["Hearts" , 2]]
STRAIGHT_FLUSH_HAND = [ ["Hearts" , 7], ["Hearts" , 5],["Hearts" , 9],["Hearts" , 6],["Hearts" , 8]]

def test_value_high_card_as():
    assert value_hand(HIGH_CARD_HAND) == 14

def test_is_three_of_a_kind():
    assert value_hand(THREE_OF_A_KIND_HAND) == 30

def test_is_straight():
    assert value_hand(STRAIGHT_HAND) == 40

def test_is_flush():
    assert value_hand(FLUSH_HAND) == 45

def test_is_full_house():
    assert value_hand(FULL_HAND) == 50

def test_is_four_of_a_kind():
    assert value_hand(FOUR_OF_A_KIND_HAND) == 60

def test_is_straight_flush():
    assert value_hand(STRAIGHT_FLUSH_HAND) == 80

def test_value_hands_sums_five_hands():
    hands = [HIGH_CARD_HAND, THREE_OF_A_KIND_HAND, STRAIGHT_HAND, FLUSH_HAND, FULL_HAND]
    assert value_hands(hands) == 179
