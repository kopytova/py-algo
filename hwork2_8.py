# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

subsequence = input('Enter some numbers: ')
required_number = input('Enter the number to search: ')
count = 0

for item in subsequence:
    if item == required_number:
        count += 1
print(f'The selected digit appears in the entered sequence {count} times.')
