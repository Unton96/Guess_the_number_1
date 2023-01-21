import random

x = random.randint(1, 100)
counter = 0

print('Welcome to the Guess the number game!\n Enter a number from 1 to 100:')


def is_valid(s):
    return s.isdigit() and 1 <= int(s) and int(s) <= 100

def is_input_num():
    while True:
        n = input()
        if is_valid(n):
            return int(n)
        else:
            print('Could you enter a number from 1 to 100, asshole?!')
counter = 0
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
            break

is_close_digit()

print('Thank you for playing in guess the number. See you...')
