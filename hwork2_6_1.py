#В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

rand_num = random.randint(0, 101)
answer = int(input('Guess a number from 0 to 100: '))
attempts = 10

while attempts > 1:
    if answer == rand_num:
        print('Congratulations, you won!')
        break
    elif answer < rand_num:
        print('This number is less than the one guessed.')
        attempts -= 1
        answer = int(input(f'{attempts} attempts left. Enter the number  from 0 to 100: '))
    else:
        print('This number is greater than the one guessed.')
        attempts -= 1
        answer = int(input(f'{attempts} attempts left. Enter the number  from 0 to 100: '))
print(f'Your attempts have ended. Hidden number is {rand_num}.')