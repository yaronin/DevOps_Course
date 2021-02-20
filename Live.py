# The function gets input of user name and prints welcome
import GuessGame
import MemoryGame
import CurrencyRouletteGame


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")


# Gets an input from the user about the game he chose
def load_game():
    game = input("""Please choose a game to play:
                1. Memory Game - a sequence of numbers will appear for 1 second and you have to
                guess it back
                2. Guess Game - guess a number and see if you chose like the computer
                3. Currency Roulette - try and guess the value of a random amount of USD in ILS
                4. Exit\n""")
    if game.isdigit() and 1 <= int(game) <= 4:
        if int(game) == 1:
            difficulty = check_difficulty()
            MemoryGame.play(difficulty)
        elif int(game) == 2:
            difficulty = check_difficulty()
            GuessGame.play(difficulty)
        elif int(game) == 3:
            difficulty = check_difficulty()
            CurrencyRouletteGame.play(difficulty)
        elif int(game) == 4:
            return

    else:
        print("Wrong value entered")
        load_game()


# Gets input from user for difficulty level for selected game
def check_difficulty():
    difficulty = input("Please choose game difficulty from 1 to 5:")
    if difficulty.isdigit() and 1 <= int(difficulty) <= 5:
        return int(difficulty)
    else:
        print("Wrong value entered")
        check_difficulty()
