import random
import string
from words import words



from words import words

def get_valid_words(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_words(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:

        print('you have ', lives, 'lives left and you have used these letters: ',''.join(used_letters), "\n")

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))


        user_letter = input('Please enter a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in the word')

        elif user_letter in used_letters:
            print("you already used that letter")

        else:
            print("invalid letter")

    #gets there when len(word_letters) == 0 or lives == 0
    if lives == 0:
        print(f"You died, sorry. The word was: {word}")
    else:
        print(f"You guessed the word! It is {word}")

hangman()




