from art import logo
from functions import deal_card, start_cards, calculate_score, compare


def play_game():
    print(logo)
    is_game_over = False
    user_cards = start_cards()
    computer_cards = start_cards()
    user_score = -1
    computer_score = -1
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("\nType 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))



while input("\nDo you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
    print('\n' * 20)
    play_game()