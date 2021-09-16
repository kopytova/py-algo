import random

rand_list = [random.randint(-50, 51) for _ in range(15)]
print(rand_list)
min_el = rand_list[0]
min_index = 0

for idx, i in enumerate(rand_list):
    if i < min_el:
        min_el = i
        min_index = idx

print(f'The minimum negative element in the list is {min_el} and its index {min_index}')
