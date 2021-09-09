'''По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.'''

x1 = float(input('Enter coordinate x1: '))
y1 = float(input('Enter coordinate y1: '))
x2 = float(input('Enter coordinate x2: '))
y2 = float(input('Enter coordinate y2: '))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(f'Equation of a straight line: {k}*x + {b}')