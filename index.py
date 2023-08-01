from random_word import RandomWords
r = RandomWords()

# Return a single random word
randomWord = r.get_random_word()

print(randomWord)

# Ask player for a letter
guess = input("Guess a letter: ").lower()

# Print right or wrong depending on letter coincidence inside selected random word
for letter in randomWord:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")