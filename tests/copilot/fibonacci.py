from functools import lru_cache


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def memoize(f):
    memo = {}
    def helper(n):
        if n not in memo:
            memo[n] = f(n)
        return memo[n]
    return helper

@memoize
def fibonacci_memoized(n):
    return fibonacci(n)

from functools import lru_cache


@lru_cache
def fibonacci_lru_cache(n):
  return fibonacci(n)

%timeit fibonacci(20)
%timeit fibonacci_memoized(20)
%timeit fibonacci_lru_cache(20)


