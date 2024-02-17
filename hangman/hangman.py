from hangmanpics import pics
from words import words
import words
import random
import string

guess = []
counter = 7
hangman = 0

def word():
    return words.words()

def blanks(word):
    for char in word:
        guess.append("_")
    print(guess)

def search(letter, word):
    # Create loop to search characters in string and return slicer
    global hangman, counter
    if letter in word:
        for ind, char in enumerate(word):
            if char == letter:
                guess[ind] = letter
            else:
                continue
    else:
        print(pics(hangman))
        hangman += 1
        counter -= 1

    return guess

print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                  
Welcome to my hangman pygame.
Warning: Difficulty level - impossible''')

# Choose random word to start
get_word = word()

# Create blanks for guesses
blanks(get_word)

while counter > 0:
    letter = input("Take a guess...").lower()
    search(letter, get_word)
    print(' '.join(guess))

    if '_' not in guess:
        print("Congratulations! You've guessed the word!")
        break
else:
    print(f"I warned you, better luck next time. The word was: {get_word}")
