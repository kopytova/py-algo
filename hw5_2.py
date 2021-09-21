'''Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как коллекция, элементы которой это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''

def hex2dec(h):
    dec_of = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    d = 0
    for i, hexdigit in enumerate(reversed(h)):
        d += 16 ** i * dec_of[hexdigit]
    return d


def dec2hex(d):
    hex_of = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
    h = ''
    while d > 16:
        h += hex_of[d % 16]
        d //= 16
    h += hex_of[d]
    return h[::-1]


hex1 = input('hex1 = ').upper()
hex2 = input('hex2 = ').upper()

hex_sum = dec2hex(hex2dec(hex1) + hex2dec(hex2))
hex_mul = dec2hex(hex2dec(hex1) * hex2dec(hex2))

print(f'sum: {hex_sum}')
print(f'mul: {hex_mul}')
