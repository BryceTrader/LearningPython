import random
import os
import re

def main():
    game_loop()

def game_loop():
    lives = ['<3', '<3', '<3', '<3', '<3', '<3', '<3', '<3', '<3']
    word = get_word()
    answer_sheet = ['_' for letters in word]
    guessed_letters = []

    playing = True
    while playing:
        guess = get_guess(lives, answer_sheet, guessed_letters)
        check_guess(guess, word, answer_sheet, lives)
        playing = answer_sheet != word
        if not lives:
            clear_console()
            print(f'You lose. The word was {"".join(word)}.')
            play_again()
            break
    if not playing:
        clear_console()
        print(f'Congrats on guessing {"".join(word)}!\nYou had {len(lives)} \
{"lives" if len(lives) > 1 else "life"} left!')
        play_again()

def get_word():
    with open("wl.txt", 'r', encoding='utf-8') as file:
        file = file.readlines()
        word = list(random.choice(file))

    word.pop() # remove newline character
    return word

def get_guess(lives, answer_sheet, guessed_letters):
    still_guessing = True

    while still_guessing and lives:
        clear_console()
        print(f'Letters that have been guessed: {" ".join(guessed_letters)}\n')
        print(f"Lives: {' '.join(lives)}")
        print(' '.join(answer_sheet) + '\n')
        guess = input('Please enter your guess: ').lower()

        valid_guess = re.search('[a-z]', guess)
        if valid_guess:
            still_guessing = has_been_guessed(guess, guessed_letters)
    return guess

def check_guess(guess, word, answer_sheet, lives):
    if guess in word:
        for i, letter in enumerate(word):
            if guess == letter:
                answer_sheet[i] = letter
    else:
        lives.pop()

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def has_been_guessed(guess, guessed_letters):
    if guess in guessed_letters or len(guess) != 1:
        return True
    guessed_letters.append(guess)
    return False

def play_again():
    again = input('\nWould you like to play again? [y/N] ').lower()
    if again == 'y':
        game_loop()

if __name__ == '__main__':
    main()
