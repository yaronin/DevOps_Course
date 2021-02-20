#   The purpose of guess game is to start a new game, cast a random number between 1 to a
#   variable called difficulty . The game will get a number input from the
#   Properties
#       1. Difficulty
#       2. Secret number

import random


#   Will generate number between 1 to difficulty and save it to secret_number.
def generate_number(difficulty):
    random_number = (random.randint(1, difficulty))
    return random_number


#   Will prompt the user for a number between 1 to difficulty and return the number.
def get_guess_from_user(difficulty):
    user_number = int(input(f"Enter number between 1 to {difficulty}:\n"))
    return user_number


#   Will compare the the secret generated number to the one prompted by the get_guess_from_user.
def compare_results(secret_number, user_number):
    if secret_number == user_number:
        return True
    else:
        return False


#   Will call the functions above and play the game. Will return True / False if the user lost or won.
def play(difficulty):
    print("Welcome to Guess Game\n")
    secret_number = generate_number(difficulty)
    user_number = get_guess_from_user(difficulty)
    if compare_results(secret_number, user_number):
        print(f"You guessed {secret_number} and won :)")
    else:
        print(f"You didn't guess {secret_number} and lost :(")
