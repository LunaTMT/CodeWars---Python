# https://www.codewars.com/kata/559a28007caad2ac4e000083
# Kata Author: g964
# 5 kyu

# code author: https://realpython.com/fibonacci-sequence-python/

cache = {0: 0, 1: 1}

def fibonacci_of(n):
    if n in cache:  # Base case
        return cache[n]
        # Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]

def perimeter(n):
      return 4 * (sum([fibonacci_of(i) for i in range(n+2)]))
