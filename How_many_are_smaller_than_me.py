# https://www.codewars.com/kata/56a1c074f87bc2201200002e/train/python
# joh_pot 
# 7 kyu


def smaller(arr):
    return [sum([1 for i in arr[idx:] if i < value]) for idx, value in enumerate(arr)]
