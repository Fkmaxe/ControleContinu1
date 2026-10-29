import pytest
from main import value_hand

HIGH_CARD_HAND = [ ["Hearts" , 1], ["Diamonds" , 3],["Spades" , 5],["Clubs" , 7],["Hearts" , 14]]
THREE_OF_A_KIND_HAND = [ ["Hearts" , 1], ["Diamonds" , 1],["Spades" , 1],["Clubs" , 7],["Hearts" , 14]]



def test_value_high_card_as():
    assert value_hand(HIGH_CARD_HAND) == 14

def test_is_three_of_a_kind():
    assert value_hand(THREE_OF_A_KIND_HAND) == 30
