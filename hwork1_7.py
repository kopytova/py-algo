'''По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.'''

a = int(input('Enter the length of the first side of the triangle: '))
b = int(input('Enter the length of the second side of the triangle: '))
c = int(input('Enter the length of the third side of the triangle: '))

if a + b <= c or a + c <= b or b + c <= a:
    print('Tiangle does not exist')
elif a == b and a == c:
    print('Equilateral triangle')
elif a == b or a == c or b == c:
    print('Isosceles triangle')
else:
    print('Versatile triangle')

