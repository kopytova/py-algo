import cProfile
import random


def max_min_changer(rand_list):
    min_el = rand_list[0]
    max_el = rand_list[0]
    min_index = 0
    max_index = 0

    for i in range(1, len(rand_list)):
        if rand_list[i] < min_el:
            min_el = rand_list[i]
            min_index = i
        if rand_list[i] > max_el:
            max_el = rand_list[i]
            max_index = i

    rand_list[min_index] = max_el
    rand_list[max_index] = min_el


def main():
    rand_list = [random.randint(1, 100) for _ in range(10000)]
    print(rand_list)
    max_min_changer(rand_list)
    print(rand_list)


cProfile.run('main()')


'''
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.095    0.095 <string>:1(<module>)
        1    0.000    0.000    0.095    0.095 hw4_1.py:23(main)
        1    0.023    0.023    0.075    0.075 hw4_1.py:24(<listcomp>)
        1    0.013    0.013    0.013    0.013 hw4_1.py:5(max_min_changer)
    10000    0.014    0.000    0.025    0.000 random.py:238(_randbelow_with_getrandbits)
    10000    0.014    0.000    0.040    0.000 random.py:291(randrange)
    10000    0.013    0.000    0.052    0.000 random.py:335(randint)
        1    0.001    0.001    0.097    0.097 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.007    0.003    0.007    0.003 {built-in method builtins.print}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12977    0.010    0.000    0.010    0.000 {method 'getrandbits' of '_random.Random' objects}



Process finished with exit code 0
'''