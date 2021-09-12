# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

num = int(input('Enter natural numbers. Press 0 to exit .\n num = '))
max_sum = 0
while num != 0:
    digit_sum = 0
    n = num
    while num % 10 != 0 or num // 10 != 0:
        digit_sum += num % 10
        num //= 10
    if digit_sum > max_sum:
        max_sum = digit_sum
        max_num = n
    num = int(input('Enter natural numbers. Press 0 to exit .\n num = '))

print(f'У числа {max_num} наибольшая сумма цифр = {max_sum}')
