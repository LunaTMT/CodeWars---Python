# https://www.codewars.com/kata/51edd51599a189fe7f000015/python
# Kata Author: kylehill
# 5 kyu

def solution(a, b):
    return sum([pow(abs(i - j), 2) for i, j in zip(a, b)]) / len(a)
