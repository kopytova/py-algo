import random

rand_list = [random.randint(1, 100) for _ in range(10)]
min_el = rand_list[0]
max_el = rand_list[0]
min_index = 0
max_index = 0

print(rand_list)

for i in range(1, len(rand_list)):
    if rand_list[i] < min_el:
        min_el = rand_list[i]
        min_index = i
    if rand_list[i] > max_el:
        max_el = rand_list[i]
        max_index = i

rand_list[min_index] = max_el
rand_list[max_index] = min_el

print(rand_list)