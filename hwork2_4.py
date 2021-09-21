# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

row = int(input('Enter the number of items: '))

i = 0
num = 1
sum = 0
while i < row:
    sum += num
    num /= -2
    i += 1

print(f'Sequence sum is {sum}')
