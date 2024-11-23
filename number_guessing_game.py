#!/usr/bin/env python3

import random

def number_guessing_game():
    """
    This function implements a number guessing game.
    """

    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    random_number = random.randint(lower_bound, upper_bound)

    print(f"Guess a number between {lower_bound} and {upper_bound}! (Enter 101 to quit)")

    guess = None
    guess_count = 0

    while True:
        try:
            guess = int(input("Your guess: "))

            if guess == 101:
                print("You have quit the game.")
                break

            guess_count += 1

            if guess < random_number:
                print("Too low.")
            elif guess > random_number:
                print("Too high.")
            else:
                print(f"Congratulations! You guessed it in {guess_count} guesses!")
                continue_game = input("Enter 1 to play again or 2 to quit: ")
                if continue_game == '1':
                    random_number = random.randint(lower_bound, upper_bound)
                    guess_count = 0
                    print(f"New number generated. Guess between {lower_bound} and {upper_bound}.")
                else:
                    print("You have quit the game.")
                    break

        except ValueError:
            print("Please enter a number or 101 to quit.")

# Start the game
number_guessing_game()
