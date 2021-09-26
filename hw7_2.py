# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

rand_list = [random.randint(0, 50) for i in range(10)]


def merge_sort(array_of_nums):
    if len(array_of_nums) < 2:
        return array_of_nums

    middle = len(array_of_nums) // 2

    first_part = merge_sort(array_of_nums[:middle])
    second_part = merge_sort(array_of_nums[middle:])

    return merge_list(first_part, second_part)


def merge_list(first_list, second_list):
    result_list = []
    i = 0
    j = 0
    while i < len(first_list) and j < len(second_list):
        if first_list[i] <= second_list[j]:
            result_list.append(first_list[i])
            i += 1
        else:
            result_list.append(second_list[j])
            j += 1

    result_list += first_list[i:]
    result_list += second_list[j:]
    return result_list


print(rand_list)
print(merge_sort(rand_list))
