import pytest
from main import value_high_card

HIGH_CARD_HAND = [ ["Hearts" , 1], ["Diamonds" , 3],["Spades" , 5],["Clubs" , 7],["Hearts" , 14]]




def test_value_high_card_as():
    assert value_high_card(HIGH_CARD_HAND) == 14