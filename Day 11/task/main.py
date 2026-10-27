import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# Use the list of cards above & return a random card
def deal_card():
    return random.choice(cards)

# It takes a List of cards as input and returns the sum of all the cards in the List as the score
def calculate_score(input_list):
    score = sum(input_list)
    # Check for blackjack [ace + 10]
    if 11 in input_list:
        for card in input_list:
            if card == 10:
                return 0
        # If it is not a blackjack then check the score, if proceeds 21 then replace 11 with 1
        if score > 21:
            input_list.remove(11)
            input_list.append(1)
            return sum(input_list)
    return score

# Compare scores
def compare(user_scores, computer_scores):
    if user_scores == computer_scores:
        return "Draw 🙃"
    elif computer_scores == 0:
        return "You lose 😤"
    elif user_scores == 0:
        return "You win 😁"
    elif user_scores > 21:
        return "You went over. You lose 😭"
    elif computer_scores > 21:
        return "Opponent went over. You win 😁"
    elif user_scores > computer_scores:
            return "You win 😁"
    else:
        return "You lose 😭"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False
    while not is_game_over:
        # Check if cards are drawn for the 1st time
        if len(user_cards) == 0:
            for _ in range(2):
                user_cards.append(deal_card())
                computer_cards.append(deal_card())
        else:
            user_cards.append(deal_card())

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            continue_play = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if continue_play != 'y':
                is_game_over = True

    # The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    final_msg = f"Your final hand: {user_cards}, final score: {sum(user_cards)}\n"
    final_msg += f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n"
    print(final_msg)

    msg = compare(user_score, computer_score)
    print(msg)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    play_game()