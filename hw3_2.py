import random
rand_list = [random.randint(0, 100) for _ in range(10)]
index_list = []

for item in rand_list:
    if item % 2 == 0:
        index_list.append(rand_list.index(item))

print(index_list)