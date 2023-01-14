# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/python
# Kata Author: kphurley
# 7 kyu
import math
def find_next_square(sq):
    n = math.pow(math.sqrt(sq) + 1, 2) 
    return n if not n != int(n) else -1
