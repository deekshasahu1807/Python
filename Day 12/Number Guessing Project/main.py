import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
system_guess = random.randint(1, 100)
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# hard: 5
# easy: 10
if difficulty_level == "easy":
    attempts = 10
else:
    attempts = 5

is_game_over = False
while not is_game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess < 0 or guess > 100:
        print("Please enter a number between 0 and 100.")
    else:
        if guess == system_guess:
            is_game_over = True
            print(f"You got it! The answer was {system_guess}.")
        elif guess > system_guess:
            print("Too high.\nGuess again.")
            attempts -= 1
        elif guess < system_guess:
            print("Too low.\nGuess again.")
            attempts -= 1

    if attempts == 0:
        is_game_over = True
        print("You've run out of guesses. Refresh the page to run again.")