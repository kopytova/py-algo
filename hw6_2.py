#hwork2_6

import random
import sys

rand_num = random.randint(1, 100)

for item in range(10):
    answer = int(input('Guess a number from 0 to 100 : '))
    if answPython 3.9.2
64 biter == rand_num:
        print('Congratulations, you won!')
        break
    elif answer < rand_num:
        print('This number is less than the one guessed.')
    else:
        print('This number is greater than the one guessed.')



    print(f'Size of random number: {sys.getsizeof(rand_num)}')
    print(f'Size of item: {sys.getsizeof(item)}')
    print(f'Size of answer: {sys.getsizeof(answer)}')

#print(f'Hidden number is {rand_num}.')

'''Guess a number from 0 to 100 : 40
This number is less than the one guessed.
Size of random number: 28
Size of item: 24
Size of answer: 28
Guess a number from 0 to 100 : 50
This number is greater than the one guessed.
Size of random number: 28
Size of item: 28
Size of answer: 28
Guess a number from 0 to 100 : 45
This number is less than the one guessed.
Size of random number: 28
Size of item: 28
Size of answer: 28
Guess a number from 0 to 100 : 48
This number is greater than the one guessed.
Size of random number: 28
Size of item: 28
Size of answer: 28
Guess a number from 0 to 100 : 47
Congratulations, you won!

Python 3.9.2
64 bit'''
