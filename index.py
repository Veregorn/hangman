# This module gives us a huge list of English words to play with
from random_word import RandomWords
r = RandomWords()

# Import os module to be able to clear console
import os

# define a function to clear console independent of OS
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII logo art
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

# ASCII hangman art
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Return a single random word
word = r.get_random_word()

# Saves word's length in another var
wordLength = len(word)

# Establish player lives
playerLives = 6

# Create a list with "_" instead of letters. Length must be the same as random word length
display = []

# Create another list with missed letters
missedLetters = []

# Initial state of 'display' is _ _ _ _ _ _ _
for _ in range(wordLength):
    display.append("_")

# we need a condition to check if all letters have been guessed
allLettersGuessed = False

# We need a var to save the letter chosen by player
guess = ""

# Delete this line when development was finished
# print(f"Pssst, the solution is {word}.")
# print("")

 # Clear console
clear_console()

# This is the main game loop
while not allLettersGuessed:

    # Print the logo of the game
    print(logo)
    print("")

    # Test if last letter has been guessed yet
    if guess in display:
        print(f"You have already guessed letter '{guess}'. Try with another one")
        print("")

    # Display letters guessed by player
    for i in range(wordLength):
        if word[i] == guess:
            display[i] = guess

    # If player hasn't guessed the letter last round and isn't first round, subs a life
    if (guess not in word) and (guess != ""):
        
        playerLives -= 1
        
        # We also have to register that letter in missed letters list (if it isn't there yet)
        if guess not in missedLetters:
            missedLetters.append(guess)

        print(f"Letter '{guess}' is not in the word. You lose a life")
        print("")

    # Print actual state of word
    print("The word is:")
    print("")
    for i in range(wordLength):
        print(display[i],end=" ")
    print("")
    print("")

    # Inform user about missed letters
    print("You have missed these letters:",end=" ")

    for letter in missedLetters:
        print(letter,end=" ")

    print("")

    # Display game state
    print(stages[playerLives])
    print("")

    # Test if game is over
    if playerLives == 0:
        print("You lose.")
        print("")
        break

    # Test if all letters have been guessed
    if "_" not in display:
        allLettersGuessed = True
        print("You win.")
        print("")
        break

    # Ask player for a letter
    guess = input("Guess a letter: ").lower()
    print("")

    # Clear console
    clear_console()