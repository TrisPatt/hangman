import random
from gallows import gallows_image
from words import words_list

number_of_guesses = 6
previous_guesses = []

def rules():
    print("These are the rules")

def start_game():
    print("Starting game...")

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

        if options == '1':
            rules()
            break
        elif options == '2':
            start_game()
            break
        elif options == '3':
            print("Exiting the game, Goodbye! ...")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

    
        

    


start_menu()



#def main():
  

