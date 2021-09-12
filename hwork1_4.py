''' Написать программу, которая генерирует в указанных пользователем границах:

    случайное целое число;
    случайное вещественное число;
    случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
'''

from random import uniform, randint

type = input('Specify data type: "i" for integer, "f" for float, "c" for characters: ')
first = input('Enter the first value: ')
second = input('Enter the second value: ')

if type == "i":
    print(randint(int(first), int(second)))
elif type == "f":
    print(uniform(float(first), float(second)))
elif type == "c":
    print(chr(randint(ord(first), ord(second))))
else:
    print('You entered an invalid character')




