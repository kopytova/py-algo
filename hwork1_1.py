'''Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.'''

num = int(input('Enter a tree_digit number: '))
sum = 0
mul = 1 # присвоили переменной значение 1 т.к. если присвоить ноль, то при дальнейшем выполнении кода при умножении полученного числа на ноль, будем получать ноль

while num > 0: # пишем цикл, который будет работать, пока переменная num больше нуля. Затем цикл останавливается.
    a = num % 10
    num = num // 10
    sum = sum + a
    mul = mul * a

print(f'The sum of the digits of the entered number: {sum}, multiplication of digits of the entered number: {mul}')


