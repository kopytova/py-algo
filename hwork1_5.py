'''Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.'''

a = input('Enter the first letter from: ').lower()
b = input('Enter the second letter: ').lower()

a = ord(a) - ord('a') + 1 # прибавляем единицу, так как в противном случае будет сдвиг влево на 1 символ и значение будет ошибочным
b = ord(b) - ord('a') + 1
c = (abs(a - b) - 1) # отнимаем единицу, так как иначе значение между буквами будет на 1 символ больше
print(f'The first letter entered is in {a} place. The second letter entered is in {b} place. There are {c} letters between entered letters.')