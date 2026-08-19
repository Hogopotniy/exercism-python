"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """
    face_cards = {"J", "Q", "K"}
    if card in face_cards:
        return 10
    elif card == "A":
        return 1
    return int(card)
    


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """
    # card_1 = 0
    # face_cards = {"J", "Q", "K"}
    # if card_one in face_cards:
    #     card_1 += 10
    # elif card_one == "A":
    #     card_1 += 1
    # else:
    #     card_1 += int(card_one)

    # card_2 = 0
    # face_cards = {"J", "Q", "K"}
    # if card_two in face_cards:
    #     card_2 += 10
    # elif card_two == "A":
    #     card_2 += 1
    # else:
    #     card_2 += int(card_two)
    
    # if card_1 > card_2:
    #     return card_one
    # elif card_1 < card_2:
    #     return card_two
    # else:
    #     return (card_one, card_two)

    
    card_1 = value_of_card(card_one)
    card_2 = value_of_card(card_two)

    if card_1 > card_2:
        return card_one
    elif card_1 < card_2:
        return card_two
    return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """
    # def value_of_card(card):
    #     if card in {"J", "Q", "K"}:
    #         return 10
    #     elif card == "A":
    #         return 11
    #     else:
    #         return int(card)
        
    # card_1 = value_of_card(card_one)
    # card_2 = value_of_card(card_two)

    # if card_1 + card_2 + 11 <= 21:
    #     return 11
    # else:
    #     return 1

    card_1 = value_of_card(card_one)
    card_2 = value_of_card(card_two)

    if card_one == "A":
        card_1 = 11

    if card_two == "A":
        card_2 = 11

    return 11 if card_1 + card_2 + 11 <= 21 else 1

    

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """

    card_1 = value_of_card(card_one)
    card_2 = value_of_card(card_two)

    if card_one == "A":
        card_1 = 11

    if card_two == "A":
        card_2 = 11

    return True if card_1 + card_2 == 21 else False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return True if value_of_card(card_one) == value_of_card(card_two) else False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    return value_of_card(card_one) + value_of_card(card_two) in {9,10,11}
