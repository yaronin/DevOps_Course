#   This game will use the free currency api to get the current exchange rate from USD to ILS, will
#   generate a new random number between 1-100 a will ask the user what he thinks is the value of
#   the generated number from USD to ILS, depending on the user’s difficulty his answer will be
#   correct if the guessed value is between the interval surrounding the correct answer

from numpy import arange
from openexchangerate import OpenExchangeRates


#   Will get the current currency rate from USD to ILS and will
#   generate an interval as follows:
#       a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t + (5 - d))
def get_money_interval(difficulty):
    d = difficulty
    client = OpenExchangeRates(api_key="36ddff57331a4f15befef4f60f473b61")
    t = round(client.latest().dict.get('ILS'), 2)
    money_interval = arange(float(t - (5 - d)), float(t + (5 - d)))
    #   print(money_interval)
    return money_interval


#   A method to prompt a guess from the user to enter a guess of
#   value to a given amount of USD
def get_guess_from_user():
    user_guess = input("Please guess the USD/ILD currency rate\n")
    return float(user_guess)


#   Will call the functions above and play the game. Will return True / False if the user lost or won.
def play(difficulty):
    money_interval = []
    money_interval = get_money_interval(difficulty)
    user_guess = float(get_guess_from_user())
    if user_guess in money_interval:
        print(f"Nice guess! The currency rate {user_guess} is correct! You won :)")
    else:
        print("Wrong currency rate.You lost the game :(")
