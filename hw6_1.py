#hwork1_3

import sys

x1 = float(input('Enter coordinate x1: '))
y1 = float(input('Enter coordinate y1: '))
x2 = float(input('Enter coordinate x2: '))
y2 = float(input('Enter coordinate y2: '))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(f'Equation of a straight line: {k}*x + {b}')

overall_size = 0
list_el = (x1, y1, x2, y2, k, b)


for el in list_el:
    overall_size += sys.getsizeof(el)

print(f'Total size of variables: {overall_size}.')

'''Enter coordinate x1: 5.2
Enter coordinate y1: 4.3
Enter coordinate x2: 8.1
Enter coordinate y2: 1.3
Equation of a straight line: -1.03448275862069*x + 9.67931034482759
Total size of variables: 144.

Python 3.9.2
64 bit'''