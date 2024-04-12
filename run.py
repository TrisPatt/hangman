import random
from gallows import gallows_image
from words import words_list


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
    print("Press ENTER to return to the main menu...")
    input()
    start_menu()

def print_gallows(incorrect_guesses, max_incorrect_guesses):
    if incorrect_guesses < len(gallows_image):
        print(gallows_image[incorrect_guesses])
    else:
        print("You lose")


def start_game():
    print("Starting game...")
    incorrect_guesses = 0
    max_incorrect_guesses = len(gallows_image) - 1
    previous_guesses = []
    hidden_word = random.choice(words_list).upper()
    hidden_letters = ["_"] * len(hidden_word)
    print("The word to guess is:", " ".join(hidden_letters))
    print_gallows(0, max_incorrect_guesses)  
        
    while incorrect_guesses <= max_incorrect_guesses:
        guess = input("Enter your guess: ").upper()
        print(f"previous guesses: {previous_guesses}")
        print(f"The word to guess is: {hidden_letters}")

        if guess in hidden_word:
            print("correct")
            for i in range(len(hidden_word)):
                if hidden_word[i] == guess:
                    hidden_letters[i] = guess
            print(f"The word to guess is:", " ".join(hidden_letters))
            if "_" not in hidden_letters: 
                print("Congratulations! You've guessed the word correctly!")
                break
            print_gallows(incorrect_guesses, max_incorrect_guesses)
                        
        else:
            print("Incorrect")
            incorrect_guesses += 1
            print_gallows(incorrect_guesses, max_incorrect_guesses)
            previous_guesses.append(guess)
            
            if incorrect_guesses > max_incorrect_guesses:
                print("You lost! You ran out of guesses.")
                break
    

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
  

