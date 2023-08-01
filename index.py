from random_word import RandomWords
r = RandomWords()

# Return a single random word
randomWord = r.get_random_word()

# Create a list with "_" instead of letters. Length must be the same as random word length
display = []
for i in range(0,len(randomWord)):
    display.append("_")

print(f"Pssst, the solution is {randomWord}.")

# Ask player for a letter
guess = input("Guess a letter: ").lower()

# Print right or wrong depending on letter coincidence inside selected random word
for i in range(0,len(randomWord)):
    if randomWord[i] == guess:
        display[i] = guess

print(display)