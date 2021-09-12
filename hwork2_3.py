# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

num = input('Enter the number: ')

if num.isdigit():
    print(f'Number {num} in reverse order: {num[::-1]}')
else:
    print(f'Only numbers are required')