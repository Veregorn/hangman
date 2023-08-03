from random_word import RandomWords
r = RandomWords()

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
# Establish win condition value to false
playerWins = False
# Establish player lives
playerLives = 6

# Create a list with "_" instead of letters. Length must be the same as random word length
display = []
wordLength = len(word)

for _ in range(wordLength):
    display.append("_")

# we need a condition to check if all letters have been guessed
allLettersGuessed = False

print(f"Pssst, the solution is {word}.")

# This is the main game loop
while not allLettersGuessed:
    # Ask player for a letter
    guess = input("Guess a letter: ").lower()

    # Display letters guessed by player
    notGuessed = True # This var controls if player has guessed some letter these round
    for i in range(wordLength):
        if word[i] == guess:
            display[i] = guess
            notGuessed = False
            
        print(display[i],end=" ")

    # If player hasn't guessed the letter this round, subs a life
    if notGuessed:
        playerLives -= 1
    
    print("")

    # Display game state
    print(stages[playerLives])

    # Test if all letters have been guessed
    if "_" not in display:
        allLettersGuessed = True
        print("You win.")

    # Test if game is over
    if playerLives == 0:
        print("You lose.")
        break