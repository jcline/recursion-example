#!/usr/bin/env python3

import timeit

def naive():
    """
    Naive recursively calls itself ad infinitum.
    Never* terminates.
    
    *: assuming infinite stack/recursion depth
    """
    naive()

def countdown(n):
    """
    Count from n to 0 recursively.
    """
    print(n)
    if n > 0:
        countdown(n-1)

def countdown_iteratively(n):
    """
    Count from n to 0 iteratively.
    """
    for i in range(n,-1,-1): # [n,-1)
        print(i)

def fibonacci(n):
    """
    Naive implementation of recursive fibonacci.
    O(nlogn)
             n
       n-1      n-2
    n-2  n-3  n-3  n-4
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

cached={}
def fibonacci_memoized(n):
    """
    O(n) implementation of recursive fibonacci

    Utilizes memoization to short-circuit additional
    branches of the recursive tree.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in cached:
        return cached[n]

    n1 = fibonacci_memoized(n-1)
    n2 = fibonacci_memoized(n-2)

    cached[n] = n1+n2
    return cached[n]

def fibonacci_iteratively(n):
    """
    Iteratively calculate fibonacci values by building a list.
    O(n)
    """
    fibs = [0,1]
    for i in range(2,n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[n]

print(timeit.timeit('fibonacci(7)', "from __main__ import fibonacci"))
print(timeit.timeit('fibonacci_memoized(7)', "from __main__ import fibonacci_memoized"))
print(timeit.timeit('fibonacci_iteratively(7)', "from __main__ import fibonacci_iteratively"))
