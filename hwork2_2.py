# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = input('Enter any number greater than zero: ')
even_numbers = 0
odd_numbers = 0

for digit in number:
    if int(digit) % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers +=1

print(f'The entered number contains {even_numbers} even digits and {odd_numbers} odd digits.')