import cProfile
import math


def without_sieve(k):
    primes_list = []
    for i in range(2, int(k * math.log(k)) + k * 10):
        is_prime = True
        for j in primes_list:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(i)
        if len(primes_list) == k:
            return i


def with_sieve(k):
    numbers = list(range(2, int(k * math.log(k)) + k * 10))
    for n in numbers:
        if n != 0:
            for p in range(2 * n, len(numbers), n):
                numbers[p - 2] = 0

    i = 0
    for n in numbers:
        if n != 0:
            i += 1
            if i == k:
                return n


cProfile.run("with_sieve(5000)")
cProfile.run("without_sieve(5000)")


'''/home/simko/PycharmProjects/pythonProject/venv/bin/python /home/simko/PycharmProjects/py-algo/hw4_2.py
         8949 function calls in 0.260 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.022    0.022    0.260    0.260 <string>:1(<module>)
        1    0.237    0.237    0.238    0.238 hw4_2.py:19(with_sieve)
        1    0.000    0.000    0.260    0.260 {built-in method builtins.exec}
     8944    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method math.log}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         53615 function calls in 1.271 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.271    1.271 <string>:1(<module>)
        1    1.262    1.262    1.270    1.270 hw4_2.py:5(without_sieve)
        1    0.000    0.000    1.271    1.271 {built-in method builtins.exec}
    48610    0.007    0.000    0.007    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method math.log}
     5000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



Process finished with exit code 0
'''