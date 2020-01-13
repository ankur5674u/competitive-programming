__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '01-13-2020'

"""

https://www.codewars.com/kata/529adbf7533b761c560004e5
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
    
The Fibonacci sequence is traditionally used to explain tree recursion.
This algorithm serves well its educative purpose but it's tremendously inefficient,
not only because of recursion, but because we invoke the fibonacci function twice,
and the right branch of recursion (i.e. fibonacci(n-2)) recalculates all the Fibonacci numbers
already calculated by the left branch (i.e. fibonacci(n-1)).

This algorithm is so inefficient that the time to calculate any Fibonacci number over 50 is simply too much.
You may go for a cup of coffee or go take a nap while you wait for the answer. But if you try it 
here in Code Wars you will most likely get a code timeout before any answers.

For this particular Kata we want to implement the memoization solution. This will be cool because it will 
let us keep using the tree recursion algorithm while still keeping it sufficiently optimized to get an 
answer very rapidly.

The trick of the memoized version is that we will keep a cache data structure (most likely an associative array)
where we will store the Fibonacci numbers as we calculate them. When a Fibonacci number is calculated,
we first look it up in the cache, if it's not there, we calculate it and put it in the cache,
otherwise we returned the cached number.

"""
from functools import wraps, lru_cache


def memoized_fibonacci(f):
    memory = {}

    @wraps(f)
    def decorated(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]
    return decorated


@memoized_fibonacci
def fibonacci(num):
    if num in [0, 1]:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


@lru_cache(None)
def fibonacci_using_built_in_decorators(num):
    if num in [0, 1]:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == '__main__':
    fibonacci_using_built_in_decorators(120)
