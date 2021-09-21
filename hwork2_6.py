#В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

rand_num = random.randint(1, 100)

for item in range(10):
    answer = int(input('Guess a number from 0 to 100 : '))
    if answer == rand_num:
        print('Congratulations, you won!')
        break
    elif answer < rand_num:
        print('This number is less than the one guessed.')
    else:
        print('This number is greater than the one guessed.')
print(f'Hidden number is {rand_num}.')