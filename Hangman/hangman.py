import random
import os

with open("wl.txt", 'r', encoding='utf-8') as file:
    file = file.readlines()
    numberOfWords = len(file) - 1
    index = random.randint(0, numberOfWords)
    word = list(file[index])

word.pop() # remove newline character
answerSheet = []
lives = ['Lives:', '<3', '<3', '<3','<3', '<3', '<3','<3', '<3', '<3']
guessed_letters = []

for l in word:
    answerSheet.append('_')


def game_loop():
    playing = True
    while playing:
        guess = get_guess()
        check_guess(guess)
        playing = is_not_solved()
        if len(lives) == 1:
            clear_console()
            print(f'You lose. The word was {"".join(word)}.')
            break
    if not playing:
        clear_console()
        print(f'Congrats on guessing {"".join(word)}!\nYou had {len(lives) - 1} lives left!')

def get_guess():
    guessing = True
    guess = ''

    while guessing and len(lives) > 1:
        clear_console()
        print(f'Letters that have been guessed: {" ".join(guessed_letters)}\n')
        print(' '.join(lives) + '\n')
        print(' '.join(answerSheet) + '\n')
        guess = input('Please enter your guess: ')

        guessing = has_been_guessed(guess)
        if len(guess) != 1:
            guessing = True
    return guess

def check_guess(guess):
    if guess in word:
        for i, letter in enumerate(word):
            if guess == letter:
                answerSheet[i] = letter
    else:
        lives.pop()

def is_not_solved():
    return answerSheet != word

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def has_been_guessed(guess):
    if guess in guessed_letters:
        return True
    guessed_letters.append(guess)
    return False

game_loop()
