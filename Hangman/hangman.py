import random
import os

def main():
    game_loop()


def game_loop():
    lives = ['<3', '<3', '<3', '<3', '<3', '<3', '<3', '<3', '<3']
    guessed_letters = []
    word = get_word()
    answer_sheet = ['_' for letters in word]

    playing = True
    while playing:
        guess = get_guess(lives, guessed_letters, answer_sheet)
        check_guess(guess, word, answer_sheet, lives)
        playing = answer_sheet != word
        if not lives:
            clear_console()
            print(f'You lose. The word was {"".join(word)}.')
            break
    if not playing:
        clear_console()
        print(f'Congrats on guessing {"".join(word)}!\nYou had {len(lives)} lives left!')

def get_word():
    with open("wl.txt", 'r', encoding='utf-8') as file:
        file = file.readlines()
        number_of_words = len(file) - 1
        index = random.randint(0, number_of_words)
        word = list(file[index])

    word.pop() # remove newline character
    return word

def get_guess(lives, guessed_letters, answer_sheet):
    guessing = True

    while guessing and lives:
        clear_console()
        print(f'Letters that have been guessed: {" ".join(guessed_letters)}\n')
        print(f"Lives: {' '.join(lives)}")
        print(' '.join(answer_sheet) + '\n')
        guess = input('Please enter your guess: ')

        guessing = has_been_guessed(guess, guessed_letters)
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

if __name__ == '__main__':
    main()
