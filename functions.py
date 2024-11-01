from random import choice, choices

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_cards() -> list[int, int]:
    """Returns a list of two card numbers."""
    return choices(cards, k=2)


def deal_card() -> int:
    """Returns a random card from the deck"""
    return choice(cards)


def calculate_score(list_of_cards: list[int, ...]) -> int:
    """Take a list of cards and return the score calculated from the cards."""
    sum_cards = sum(list_of_cards)

    if sum_cards == 21 and len(list_of_cards) == 2:
        return 0

    if 11 in list_of_cards and sum_cards > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)

    return sum_cards


def compare(user_score: int, computer_score: int) -> str:
    """Takes two numbers and compares them. Returns a string with a message about winner."""
    if user_score == computer_score:
        return f"Draw"
    elif computer_score == 0:
        return f"Lose, opponent has Blackjack"
    elif user_score == 0:
        return f"Win with a Blackjack!"
    elif user_score > 21:
        return f"You went over. You lose!"
    elif computer_score > 21:
        return f"Opponent went over. You win!"
    elif user_score > computer_score:
        return f"You win!"
    else:
        return f"You lose!"