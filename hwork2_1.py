
while True:
    example = (input('Enter the example to be solved. Press 0 to exit the program.\n '))
    if example == '0':
        break
    list_example = example.split()
    num1 = int(list_example[0])
    num2 = int(list_example[2])
    operand = list_example[1]
    if operand == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operand == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operand == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operand == '/':
        if num2 == 0:
            print('Divisor cannot be 0 ')
        else:
            print(f'{num1} / {num2} = {num1 / num2}')
    else:
        print('Wrong operand')

