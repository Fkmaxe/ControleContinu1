from main import Card, HEARTS, DIAMONDS, CLUBS, SPADES, hand_points, total_points

HIGH_CARD_HAND = [Card(HEARTS, 2), Card(DIAMONDS, 3), Card(SPADES, 5), Card(CLUBS, 7), Card(HEARTS, 14)]
THREE_OF_A_KIND_HAND = [Card(HEARTS, 2), Card(DIAMONDS, 2), Card(SPADES, 2), Card(CLUBS, 7), Card(HEARTS, 14)]
STRAIGHT_HAND = [Card(HEARTS, 4), Card(DIAMONDS, 2), Card(SPADES, 5), Card(CLUBS, 6), Card(HEARTS, 3)]
FLUSH_HAND = [Card(HEARTS, 4), Card(HEARTS, 12), Card(HEARTS, 5), Card(HEARTS, 8), Card(HEARTS, 3)]
FULL_HOUSE_HAND = [Card(SPADES, 4), Card(HEARTS, 4), Card(HEARTS, 5), Card(SPADES, 5), Card(CLUBS, 5)]
FOUR_OF_A_KIND_HAND = [Card(HEARTS, 9), Card(DIAMONDS, 9), Card(SPADES, 9), Card(CLUBS, 9), Card(HEARTS, 2)]
STRAIGHT_FLUSH_HAND = [Card(HEARTS, 7), Card(HEARTS, 5), Card(HEARTS, 9), Card(HEARTS, 6), Card(HEARTS, 8)]
THREE_OF_A_KIND_IN_MIDDLE_HAND = [Card(CLUBS, 9), Card(HEARTS, 2), Card(SPADES, 2), Card(DIAMONDS, 2), Card(CLUBS, 13)]


def test_high_card_scores_highest_card_value():
    assert hand_points(HIGH_CARD_HAND) == 14

def test_three_of_a_kind_scores_30():
    assert hand_points(THREE_OF_A_KIND_HAND) == 30

def test_three_of_a_kind_not_at_start_of_hand_scores_30():
    assert hand_points(THREE_OF_A_KIND_IN_MIDDLE_HAND) == 30

def test_straight_scores_40():
    assert hand_points(STRAIGHT_HAND) == 40

def test_flush_scores_45():
    assert hand_points(FLUSH_HAND) == 45

def test_full_house_scores_50():
    assert hand_points(FULL_HOUSE_HAND) == 50

def test_four_of_a_kind_scores_60():
    assert hand_points(FOUR_OF_A_KIND_HAND) == 60

def test_straight_flush_scores_80():
    assert hand_points(STRAIGHT_FLUSH_HAND) == 80

def test_total_points_sums_every_hand():
    hands = [HIGH_CARD_HAND, THREE_OF_A_KIND_HAND, STRAIGHT_HAND, FLUSH_HAND, FULL_HOUSE_HAND]
    assert total_points(hands) == 179
