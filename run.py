import random
import os

from gallows import gallows_image
from words import words_list


def rules():
    """
    Display the rules of the game and return to the main menu.
    """
    clear_screen()
    print("----------------------------------------------------------------")
    print("                       How to play!")
    print("----------------------------------------------------------------")
    print("""
    Hangman is a word guessing game. The aim is to guess the hidden
    word before your lives run out.
    Guess a letter. If the letter is in the hidden word, it will be displayed
    in the position it occupies in that word. If it is not in the word,
    you will lose a life, and another part of the hangman will be revealed.
    The previously guessed letters will be displayed.
    You have 6 lives.
    If you make 6 incorrect guesses, you lose.
    If you guess the word before the hangman is complete, you win!
    The word will be the name of a movie title""")
    print("----------------------------------------------------------------")
    print("Press ENTER to return to the main menu...")
    input()
    start_menu()


def print_gallows(incorrect_guesses, max_incorrect_guesses):
    """
    Prints the status of the gallows taken from the list in gallows.py
    depending on the number of incorrect guesses.
    """
    if incorrect_guesses < len(gallows_image):
        print(gallows_image[incorrect_guesses])
    else:
        print("-------------------")


def clear_screen():
    """
    Clears the terminal after each guess. The OS module is imported, allowing
    the function to operate on different operating systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def return_main_menu():
    """
    While loop with a question returning 2 possible answers and error handling.
    Converts the input to lowercase.
    """
    while True:
        menu_return = input("""Would you like to return to the main menu? y/n:
        \n""").lower()

        if menu_return == 'y':
            start_menu()
            break
        elif menu_return == 'n':
            print("Thank you for playing!")
            exit()
            break
        else:
            print("Please press 'y' or 'n'")


def multiple_letter(word, letter):
    """
    Iterates over each character in the word using a for loop combined with
    enumerate to access both the character and its index in the word.

    Returns a list containing the indices (positions) where the letter occurs
    in the word.
    If the letter does not occur in the word, an empty list is returned.
    """
    multiple = []
    for i, char in enumerate(word):
        if char == letter:
            multiple.append(i)
    return multiple


def start_game():
    """
    This function starts the Hangman game.

    Generates a random word from the 'words_list' and converts it to uppercase
    in order to validate it against the user's guess, which is also converted
    to uppercase on input.

    Displays the game's visual elements including the gallows, the word to
    guess, and the previous incorrect guesses.

    Runs a while loop until the maximum number of incorrect guesses is reached
    or the user wins.
    Within the loop, it validates the user input, updates the gallows and
    previous guesses, and shows the progress of the game.
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

        # Check if the input is not more than one character or not alphabetic.
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid option. Please enter a single letter\n")
            print("The word to guess is:", " ".join(hidden_letters))
            print_gallows(incorrect_guesses, max_incorrect_guesses)
            print(f"Incorrect guesses: ", " ".join(previous_guesses))
            continue

        # Check if the input is in the previous guesses list.
        if guess in previous_guesses:
            print("You've already guessed that!\n")
            print("The word to guess is:", " ".join(hidden_letters))
            print_gallows(incorrect_guesses, max_incorrect_guesses)
            print(f"Incorrect guesses: ", " ".join(previous_guesses))
            continue

        """ Iterate through each index of the hidden word to check for
        multiple occurrences of the guessed letter. """
        if guess in hidden_word:
            print("Correct!!\n")
            multiple = multiple_letter(hidden_word, guess)
            for index in multiple:
                hidden_letters[index] = guess
            print(f"The word to guess is:", " ".join(hidden_letters))

            # Check if all letters have been guessed correctly.
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

            # Check if maximum guesses reached.
            if incorrect_guesses > max_incorrect_guesses:
                print("You lost! You ran out of guesses.\n")
                print(f"The word you were looking for is {hidden_word} !")
                return_main_menu()


def start_menu():
    """
    Creates the introduction and provides 3 options to the user with a
    while loop to limit the input to the 3 choices only.

    Provides a way of exiting the game, rules, and starting the game.
    """
    print("-----------------------------------")
    print("Welcome to Hangman! - Movie edition")
    print("-----------------------------------")
    print('''
          +---+
          |   |
              |
              |
              |
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


