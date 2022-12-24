# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
# Kata Author: marcinbunsch
# 6 kyu

def array_diff(a, b):
    return list(filter(lambda x: (x not in b), a))

if __name__ == "__main__":
    array_diff([1, 2, 2], [2])
    array_diff([1,2,3], [1, 2]) #, [3],
