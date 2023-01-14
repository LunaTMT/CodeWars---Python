# https://www.codewars.com/kata/53a1eac7e0afd3ad3300008b/python
# Kata Author: dnolan
# 6 kyu

def f(n): return n - m(f(n-1)) if n else 1

def m(n): return n - f(m(n-1)) if n else 0

if __name__ == "__main__":
    f(5)#,3)
