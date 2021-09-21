import random

rand_list = [random.randint(0, 100) for _ in range(10)]
print(rand_list)

min_el = rand_list[0]
max_el = rand_list[0]
min_index = 0
max_index = 0
summ = 0

for idx, i in enumerate(rand_list):
    if i <= min_el:
        min_el = i
        min_index = idx
    if i >= max_el:
        max_el = i
        max_index = idx

print(min_el, min_index, max_el, max_index)

if min_index > max_index:
    max_index, min_index = min_index, max_index

for i in range(min_index + 1, max_index):
    summ += rand_list[i]

print(f'The sum of the elements between the minimum and maximum elements is {summ}')




