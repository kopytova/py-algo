
import random

array_length = int(input('Enter a number: '))
rand_list = [random.randint(0, 100) for _ in range(2 * array_length + 1)]


def median(array):
    middle = len(array) // 2
    array.sort()
    if not len(array) % 2:
        return (array[middle - 1] + array[middle]) / 2
    return array[middle]


print(f'Random array:\n {rand_list}')
print(f'Median: \n {median(rand_list)}')
