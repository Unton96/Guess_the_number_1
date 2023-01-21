import random

x = random.randint(1, 100)
right_border = 100
counter = 0

print('Welcome to the Guess the number game!\n Enter a number from 1 to', right_border, ':')


def is_valid(s):
    return s.isdigit() and 1 <= int(s) and int(s) <= right_border

def is_input_num():
    while True:
        n = input()
        if is_valid(n):
            return int(n)
        else:
            print('Could you enter a number from 1 to', right_border, 'asshole?!')

def is_close_digit():
    num = is_input_num()
    global counter
    counter += 1
    while True:
        if num < x:
            print('Your number is less than the guessed number, try again')
            return is_close_digit()
        elif num > x:
            print('Your number is higher than the guessed number, try again')
            return is_close_digit()
        else:
            print('Congratulations! You guessed it! ', 'You guessed it on the', counter, 'try')
            print('Do you wanna play again?("yes"/"no")')
            break

is_close_digit()

def exit_game():
    while True:
        ans_game = input()
        global right_border
        if exit_game_valid(ans_game) and ans_game == 'yes':
            print('Enter a biggest number:')
            right_border = int(input())
            global x, counter
            x = random.randint(1, right_border)
            counter = 0
            print('Try to guess again, enter the number:')
            is_close_digit()
        elif exit_game_valid(ans_game) and ans_game == 'no':
            print('Thank you for playing in guess the number!')
            break
        else:
            print('Please enter the "yes" or "no"')

def exit_game_valid(n):
    return n == 'yes' or n == 'no'

exit_game()







