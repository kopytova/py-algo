import random

rand_list = [random.randint(1, 10) for _ in range(20)]
print(rand_list)

most_frequent = 0
for i in rand_list:
    if rand_list.count(most_frequent) < rand_list.count(i):
        most_frequent = rand_list.count(i)

print(f'The most common number in list: {most_frequent}')