import random
import os
from gallows import gallows_image
from words import words_list


def rules():
    """
    Display the rules of the game and return to the main menu
    """
    clear_screen()
    print("----------------------------------------------------------------")
    print("                       How to play!")
    print("----------------------------------------------------------------")
    print("""
    Hangman is a word guessing game. The aim is to guess the hidden 
    word before your lives run out.
    Guess a letter. If the letter is in the hidden word then this will be 
    displayed in the position it is in that word. If it is not in the word 
    then you will lose a life and another part of the hangman will be revealed. 
    The previous guessed letters will be displayed. 
    You have 6 lives. 
    If you get 6 incorrect answers then you lose.
    If you guess the word before the hangman is complete then you win!
    The word will be the name of a movie title""")
    print("----------------------------------------------------------------")
    print("Press ENTER to return to the main menu...")
    input()
    start_menu()


def print_gallows(incorrect_guesses, max_incorrect_guesses):
    """
    Prints the status of the gallows depending on the number of incorrect 
    guesses
    """
    if incorrect_guesses < len(gallows_image):
        print(gallows_image[incorrect_guesses])
    else:
        print("-------------------")


def clear_screen():
    """
    Clear the terminal after each guess. The OS module is imported which 
    allows for the function to operate on different operating systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def return_main_menu():
    """
    Asks users if they wish to return to the main menu
    """
    while True:
        menu_return = input("""Would you like to return to the main menu? y/n: \n""")
    
        if menu_return.lower() == 'y':
            start_menu()
            break
        elif menu_return.lower() == 'n':
            print("Thank you for playing!")
            exit()
            break
        else:
            print("please press 'y' or 'n'")

def multiple_letter(word, letter):
    """
    validates multiple letters in a word
    """
    multiple = []
    for i, char in enumerate(word):
        if char == letter:
            multiple.append(i)
    return multiple


def start_game():
    """
    Generate a random word from words_list.py and convert to uppercase
    in order to validate it against the user guess, which is also 
    converted to upercase on input. 
    Create the game visual display showing the gallows, the word to guess, 
    previous incorrect guesses.
    Run a while loop which runs until the maximum incorrect guesses is 
    reached or the user wins. This validates the input and shows game 
    progress, updating gallows and previous incorrect guesses.
    """
    clear_screen()
    print("Starting game...\n")
    incorrect_guesses = 0
    max_incorrect_guesses = len(gallows_image) - 2
    previous_guesses = []
    hidden_word = random.choice(words_list).upper()
    hidden_letters = ["_"] * len(hidden_word)
    print("The word to guess is:", " ".join(hidden_letters))
    print_gallows(0, max_incorrect_guesses)  
        
    while incorrect_guesses <= max_incorrect_guesses:
        guess = input("Enter your guess: \n").upper()
        clear_screen()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid option. Please enter a single letter\n")
            print_gallows(incorrect_guesses, max_incorrect_guesses)
            print(f"Incorrect guesses: ", " ".join(previous_guesses))  
            print("The word to guess is:", " ".join(hidden_letters)) 
            continue   

        if guess in previous_guesses:
            print("You've already guessed that!\n")
            print("The word to guess is:", " ".join(hidden_letters))
            print_gallows(incorrect_guesses, max_incorrect_guesses)
            print(f"Incorrect guesses: ", " ".join(previous_guesses))
            continue

        if guess in hidden_word:
            print("Correct!!\n")
            multiple = multiple_letter(hidden_word, guess)
            for index in multiple:
                hidden_letters[index] = guess
            print(f"The word to guess is:", " ".join(hidden_letters))

            if "_" not in hidden_letters: 
                print("Congratulations! You've guessed the word correctly!\n")
                return_main_menu()
            
            print_gallows(incorrect_guesses, max_incorrect_guesses)
            print(f"Incorrect guesses: ", " ".join(previous_guesses))
                        
        else:
            print("Incorrect\n")
            incorrect_guesses += 1
            print("The word to guess is:", " ".join(hidden_letters))
            print_gallows(incorrect_guesses, max_incorrect_guesses)
            previous_guesses.append(guess)
            print(f"Incorrect guesses: ", " ".join(previous_guesses))
            
            if incorrect_guesses > max_incorrect_guesses:
                print("You lost! You ran out of guesses.\n")
                print(f"The word you were looking for is {hidden_word} !")
                return_main_menu()
                
            
def start_menu():
    """
    Create the introduction and provide 3 options to the user with a 
    while loop to limit the input to the 3 choices only.
    provides a way of exiting the game, rules and staring the game
    """
    print("-----------------------------------")
    print("Welcome to Hangman! - Movie edition")
    print("-----------------------------------")
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
        options = input("Enter: \n")

        if options == '1':
            rules()
            break
        elif options == '2':
            start_game()
            break
        elif options == '3':
            print("Exiting the game, Goodbye! ...")
            exit()
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

    
start_menu()
  

