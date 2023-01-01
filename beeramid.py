# https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/python
# Kata Author: kylehill
# 5 kyu

def beeramid(bonus, price):
    
    if bonus <= 0:
        return 0
    
    level = 1
    while bonus >= 0:
        bonus -= price * pow(level, 2)
        level += 1
    return level - 2
