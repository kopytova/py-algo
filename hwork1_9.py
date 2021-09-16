'''. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).'''

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

list_of_numbers = [a, b, c]
list_of_numbers.sort() # сортируем список, составленный из введенных пользователем трех чисел
print(list_of_numbers[1])