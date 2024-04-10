import random
from gallows import gallows_image
from words import words_list

number_of_guesses = 6
previous_guesses = []

def rules():
    print("--------------------")
    print("How to play!")
    print("--------------------")
    print("Hangman is a word guessing game. The aim is to guess the hidden word \nbefore all the body parts of the man are revealed.")
    print("Guess a letter. If the letter is in the hidden word then this will \nbe displayed in the position it is in that word. If it is not in the \nword then you will lose a life and another part of the man will be \nrevealed.")
    print("The previous guessed letters will be displayed.")
    print("You have 6 lives. If you get 6 incorrect answers then you lose.")
    print("If you guess the word before the hangman is complete then you win!")
    print("--------------------")
    print("Press return to return to the main menu...")
    input()
    start_menu()

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
  

