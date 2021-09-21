import random

rand_list = [random.randint(0, 100) for _ in range(10)]
print(rand_list)

first_min_el = rand_list[0]
second_min_el = rand_list[1]

for i in rand_list:
    if i < first_min_el:
        second_min_el = first_min_el
        first_min_el = i
    elif i <= second_min_el:
        second_min_el = i

print(f'Smallest element is {first_min_el}, second smallest element is {second_min_el}.')