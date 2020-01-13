__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '01-13-2020'

from functools import wraps, lru_cache


def memoized_factorial(f):
    memory = {}

    @wraps(f)
    def decorated(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]

    return decorated


@memoized_factorial
def factorial(num):
    if num in [0, 1]:
        return num
    return num * factorial(num - 1)


@lru_cache()
def factorial_using_built_in_decorator(num):
    if num in [0, 1]:
        return num
    return num * factorial(num - 1)


if __name__ == '__main__':
    factorial_using_built_in_decorator(120)
