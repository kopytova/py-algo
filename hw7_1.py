#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random

rand_list = [random.randint(-100, 100) for item in range(10)]

def bubble_sort(array_of_nums):
    n = 1
    while n < len(rand_list):
        for i in range(len(rand_list) - n):
            if rand_list[i] < rand_list[i+1]:
                rand_list[i], rand_list[i+1] = rand_list[i+1], rand_list[i]
        n += 1


print(rand_list)
bubble_sort(rand_list)
print(rand_list)