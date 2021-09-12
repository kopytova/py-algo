'''Пользователь вводит номер буквы в алфавите. Определить, какая это буква.'''

letter_num = int(input('Enter the letter number in the alphabet from a to z: '))
char = chr(letter_num + 96)

print(char)
