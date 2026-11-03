import art
import game_data
import random

data = game_data.data
data_length = len(data)

print(art.logo)
choice_a = random.randint(0, data_length)
choice_b = random.randint(0, data_length)
while choice_a == choice_b:
    choice_b = random.randint(0, data_length)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}."

def compare(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

is_game_over = False
score = 0
while not is_game_over:
    print(f"Compare A: {format_data(data[choice_a])}")
    print(art.vs)
    print(f"Against B: {format_data(data[choice_b])}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    # Clear the screen
    print("\n" * 20)
    print(art.logo)

    compared_result = compare(user_choice, data[choice_a]['follower_count'], data[choice_b]['follower_count'])

    if compared_result:
        score += 1
        choice_a = choice_b
        choice_b = random.randint(0, data_length)
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        is_game_over = True