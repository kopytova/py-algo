# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


first_char = 32
last_char = 127
counter = 0

for item in range(first_char, last_char + 1):
    counter += 1
    if counter % 10 == 0:
        print('\n')

    print(f'{item} - {chr(item)}')
