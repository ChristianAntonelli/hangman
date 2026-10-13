#HANGMAN in Python
import random

def show_hangman(hangman_art, errors):
    for line in hangman_art[errors]:
        print(line)

def welcoming_sequence():
    print("Welcome to the Hangman game.")
    print("We will show you the firts and last letters of a word, and letter by letter you have to guess it.")
    print("You have right to 6 wrong guesses, either letters or the final word.")
    print("Good luck!")
    print()
    print()

def current_guessed_word(word):
  guessed_letters = []
  for letter in word:
     if letter in guessed_letters:
         guessed_word += letter
     else:
         guessed_word += "_"
  return guessed_word



def main():
    words = ("apple", "banana", "coconut", "pear")
    hangman_art = {0: ("   ",
                   "   ",
                   "   "),
                   1: (" O ",
                   "   ",
                   "   "),
                2: (" O ",
                   " | ",
                   "   "),
                3: (" O ",
                   "/| ",
                   "   "),
                4: (" O ",
                   "/|\\",
                   "   "),
                5: (" O ",
                   "/|\\",
                   "/  "),
                6: (" O ",
                   "/|\\",
                   "/ \\")}

    welcoming_sequence()

    word = random.choice(words)
    print(f"#For the developer: word is: {word}#")
    errors = 0
    guessed_word = "" 
    guessed_letters = [] 


    print("Your word:")
    print()
    guess = input("Guess the word or type in a letter that might be in it: ")

    while errors < 6:
    
        if guess == word:
            print(f"Congrats, the word was exactly {word}!") #RIGHT WORD

        elif (len(guess) > 1 and not len(guess) == len(word)) or len(guess) < 1: #INVALID VALUE
            print(f"'{guess}' is not a valid. Please type in either the full word or a single letter.")
            print(f"You have made {errors} mistakes and you have got {6 - errors} more shots.")

        elif guess in word and guess not in guessed_word: #RIGHT LETTER
            print(f"You got the letter {guess} right, keep going!")
            print(f"You have made {errors} mistakes and you have got {6 - errors} more shots.")
            guessed_letters.append(guess)

        elif guess not in word and not guess in guessed_word: #WRONG LETTER
            print(f"Sorry, the letter {guess} is not in the final word.")
            errors += 1
            print(f"You have made {errors} mistakes and you have got {6 - errors} more shots.")

        elif len(guess) == len(word) and not guess == word: #WRONG WORD
            print(f"Sorry, {guess} is not the correct word.")
            errors += 1
            print(f"You have made {errors} mistakes and you have got {6 - errors} more shots.")



if __name__ == "__main__":
    main()
