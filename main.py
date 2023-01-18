import random

x = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку!\nВведите число от 1 до 100:\n')


def is_valid(s):
    return s.isdigit() and 1 <= int(s) and int(s) <= 100

def is_input_num():
    while True:
        n = input()
        if is_valid(n):
            return int(n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

def is_close_digit():
    num = is_input_num()
    counter = 0
    while True:
        if num < x:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            return is_close_digit()
        elif num > x:
            print('Ваше число больше загаданного, попробуйте еще разок')
            return is_close_digit()
        else:
            print('Вы угадали, поздравляем!', 'Вы отгадали с', counter, 'попыток')
            break

is_close_digit()

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
