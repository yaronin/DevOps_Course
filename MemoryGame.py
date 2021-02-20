#   The purpose of memory game is to display an amount of random numbers to the users for 0.7
#   seconds and then prompt them from the user for the numbers that he remember. If he was right
#   with all the numbers the user will win otherwise he will lose

import random
import os
from time import sleep


#   Will generate a list of random numbers between 1 to 101.
#   The list length will be difficulty
def generate_sequence(difficulty):
    sequence = random.sample(range(1, 50), difficulty)
    return sequence


#   Will return a list of numbers prompted from the user. The list length
#   will be in the size of difficulty
def get_list_from_user(difficulty):
    sequence = []
    print(f"Enter list of {difficulty} numbers\n")
    for i in range(0, difficulty):
        num = int(input())
        sequence.append(num)
    return sequence


#   Function to compare two lists if they are equal. The function will return True / False.
def is_list_equal(random_sequence, user_sequence):
    random_sequence.sort()
    user_sequence.sort()
    if random_sequence == user_sequence:
        return True
    else:
        return False


#   Will call the functions above and play the game. Will return True / False if the user lost or won
def play(difficulty):
    print("Welcome to Memory Game\n")
    random_sequence = generate_sequence(difficulty)
    print(random_sequence)
    sleep(3)
    os.system('cls')
    user_sequence = get_list_from_user(difficulty)
    if is_list_equal(random_sequence, user_sequence):
        print("You remember correct and Won :)")
    else:
        print("Hmm...You didn't remember and lost :(")
