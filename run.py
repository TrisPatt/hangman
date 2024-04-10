import random
from gallows import gallows_image
from words import words_list

number_of_guesses = 6
previous_guesses = []

def start_menu():
    print("--------------------")
    print("Welcome to Hangman!")
    print("--------------------")
    print('''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''')
    while True:
        print("Please select an option: ")
        print(" 1. How to play")
        print(" 2. Start the game!")
        print(" 3. Quit")
        options = input("Enter: ")

        if options in ["1", "2", "3"]:
            return int(options)
        else:
            print("Please select either 1, 2 or 3")

    


start_menu()



#def main():
  

